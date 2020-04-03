import pandas as pd
from datetime import datetime
import matplotlib
import selfAnalyserUtil

dataframe = pd.read_csv("tables/time_sheet.csv")

print("Self Analyser")

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
            dataframe['time to bed'].loc[dataframe.shape[0]-1]  = bedTime
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
    userInput = int(input(("""
    ###################################
    1.Log time sheet
    2.View Statistics
    Enter your choice: """)))

    if userInput == 1:
        categories = dataframe.columns
        loggedCategories = fill24Hours(categories)
        if bool(loggedCategories):
            dataframe = dataframe.append(loggedCategories,ignore_index=True)

    print(dataframe.head())

    dataframe.to_csv("tables/time_sheet.csv",index = False)
    