import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import selfAnalyserUtil


def fill24Hours(categories):
    try:
        totalTime = 24.0
        loggedTime = 0.0
        loggedCategories = {}
        currentDate = datetime.now().date()
        lastDateInDf = dataframe['date'].loc[dataframe.shape[0]-1]
        isNewDate = currentDate > datetime.strptime(lastDateInDf,'%Y-%m-%d').date()
        if not isNewDate:
            userChoice = input("You have already logged the timesheet today.\nIf you wish to log time again enter 'y' else press any other key to skip.\nNOTE : Old log will be deleted.\n")
            if userChoice.lower() == 'y':
                dataframe.drop(dataframe.tail(1).index,inplace=True)
                isNewDate = True
        if isNewDate:
            bedTime = selfAnalyserUtil.formatTime(input("Enter the time you went to bed yesterday (in 11:00P.M. format) : "))
            dataframe.at[dataframe.shape[0]-1 , 'time to bed']  = bedTime
            wakeUpTime = selfAnalyserUtil.formatTime(input("Enter the time you woke up today (in 6:00A.M. format) : "))
            loggedCategories['sleep'] = selfAnalyserUtil.getTimeDifferenceInhours(bedTime, wakeUpTime)
            print(loggedCategories['sleep'])
            loggedTime = loggedTime + loggedCategories['sleep']
            loggedCategories['date'] = str(currentDate)
            loggedCategories['wakeup time'] = wakeUpTime

            while True:
                [print("{} {}".format(ind+1,val)) for ind,val in enumerate(categories[3:-1])]
                select = int(input("Log your 24 hours under these categories!! -- Remaining time : {}\n".format(totalTime-loggedTime)))
                currentCategory = categories[select+2]
                hour = input("Enter q to log remaining time in {0} .\nOr Enter the time spent in {0} - ".format(currentCategory))
                if hour == "q":
                    hour = totalTime - loggedTime
                hour = float(hour)
                if currentCategory not in loggedCategories:
                    loggedCategories[currentCategory] = round(hour,2)
                    loggedTime = loggedTime + hour
                    print(loggedTime)
                else:
                    loggedCategories[currentCategory] = hour

                if loggedTime == totalTime:
                    print("Thanks for logging")
                    print(loggedCategories)
                    break
                
                print(loggedCategories)
            return loggedCategories
        else:
            return loggedCategories
    except Exception as error:
        print(error)
        raise error

if __name__ == "__main__":
    
    dataframe = pd.read_csv("tables/time_sheet_master.csv")

    categories = dataframe.columns
    while True:
        userInput = int(input(("""
        Self Analyser
        ###################################
        1.Log time sheet
        2.View Statistics
        3.Quit
        Enter your choice: """)))

        if userInput == 1:
            
            loggedCategories = fill24Hours(categories)
            if bool(loggedCategories):
                dataframe = dataframe.append(loggedCategories,ignore_index=True)

            print(dataframe.head())
            
            dataframe.to_csv("tables/time_sheet.csv",index = False)

        if userInput == 2:
            userChoice = input("""
            1. Time spent on each day in particular category
            2. Time spent on last logged day in each category
            """)
            if userChoice == "1":
                [print("{} {}".format(ind+1,val)) for ind,val in enumerate(categories[3:-1])]
                select = int(input("Select the category!!"))
                currentCategory = categories[select+2]
                plt.bar(dataframe.date,dataframe[currentCategory])
                plt.xlabel("date")
                plt.ylabel("time spent on learing in hours")
                plt.title("Time spent on learning each day")
                plt.show()
            elif userChoice == "2":
                pieChart = dataframe.tail(1)
                pieChart.is_copy = False
                pieChart.dropna(axis='columns',inplace=True)
                labels = pieChart.columns[2:]
                sizes = pieChart.values[-1].tolist()[2:]
                fig1, ax1 = plt.subplots()
                ax1.pie(sizes, labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.title(dataframe.date.iloc[dataframe.shape[0]-1])
                plt.show()
        if userInput == 3:
            print("See you soon.Byee!!")
            break


    