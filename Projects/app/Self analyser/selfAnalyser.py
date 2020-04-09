import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import selfAnalyserUtil

def analyseMindSet(categories):
    try:
        loggedCategories = {}
        lastDateInDf = mindsetDf['date'].loc[mindsetDf.shape[0]-1]
        currentDate = datetime.now().date()
        isNewDate = currentDate > datetime.strptime(lastDateInDf,'%Y-%m-%d').date()
        if not isNewDate:
            userChoice = input("You have already rated your mindset today.\nIf you wish to rate again enter 'y' else press any other key to skip.\nNOTE : Old log will be deleted.\n")
            if userChoice.lower() == 'y':
                mindsetDf.drop(mindsetDf.tail(1).index,inplace=True)
                isNewDate = True
        if isNewDate:
            loggedCategories['date'] = currentDate
            while True:
                for val in categories[1:]:
                    loggedCategories[val] = int(input("Rate your {} out of 5 - ".format(val)))
                
                print(loggedCategories)
                break
            return loggedCategories
        else:
            return loggedCategories
    except Exception as e:
        print(e)
    


def logPyTimeSheet(pyModules, pyTimeLogged):
    try:
        loggedTime = 0.0
        loggedPyModules = {}
        currentDate = datetime.now().date()
        lastDateInDf = pythonDf['date'].loc[pythonDf.shape[0]-1]
        isNewDate = currentDate > datetime.strptime(lastDateInDf,'%Y-%m-%d').date()
        if not isNewDate:
            userChoice = input("You have already logged the python timesheet today.\nIf you wish to log time again enter 'y' else press any other key to skip.\nNOTE : Old log will be deleted.\n")
            if userChoice.lower() == 'y':
                pythonDf.drop(pythonDf.tail(1).index,inplace=True)
                isNewDate = True
        if isNewDate:
            loggedPyModules['date'] = currentDate
            while True:
                [print("{} {}".format(ind+1,val)) for ind,val in enumerate(pyModules[1:])]
                select = int(input("Log your {} hours under these Modules!! -- Remaining time : {}\n".format(pyTimeLogged,pyTimeLogged-loggedTime)))
                currentPyModule = pyModules[select]
                hour = input("Enter q to log remaining time in {0} .\nOr Enter the time spent in {0} - ".format(currentPyModule))
                if hour == "q":
                    hour = pyTimeLogged - loggedTime
                hour = float(hour)
                if currentPyModule not in loggedPyModules:
                    loggedPyModules[currentPyModule] = round(hour,2)
                    loggedTime = loggedTime + hour
                    print(loggedTime)
                else:
                    loggedPyModules[currentPyModule] = hour

                if loggedTime == pyTimeLogged:
                    print("Thanks for logging")
                    print(loggedPyModules)
                    break
                
                print(loggedPyModules)
            return loggedPyModules
        else:
            return loggedPyModules

    except Exception as e:
        print(e)

def logLearningTimeSheet(techCategories,totalTime):
    try:
        loggedTime = 0.0
        loggedTechCatergories = {}
        currentDate = datetime.now().date()
        lastDateInDf = learningDf['date'].loc[learningDf.shape[0]-1]
        isNewDate = currentDate > datetime.strptime(lastDateInDf,'%Y-%m-%d').date()
        if not isNewDate:
            userChoice = input("You have already logged the learning timesheet today.\nIf you wish to log time again enter 'y' else press any other key to skip.\nNOTE : Old log will be deleted.\n")
            if userChoice.lower() == 'y':
                learningDf.drop(learningDf.tail(1).index,inplace=True)
                isNewDate = True
        if isNewDate:
            loggedTechCatergories['date'] = currentDate
            while True:
                [print("{} {}".format(ind+1,val)) for ind,val in enumerate(techCategories[1:])]
                select = int(input("Log your {} hours under these categories!! -- Remaining time : {}\n".format(totalTime,totalTime-loggedTime)))
                currentTechCategory = techCategories[select]
                hour = input("Enter q to log remaining time in {0} .\nOr Enter the time spent in {0} - ".format(currentTechCategory))
                if hour == "q":
                    hour = totalTime - loggedTime
                hour = float(hour)
                if currentTechCategory not in loggedTechCatergories:
                    loggedTechCatergories[currentTechCategory] = round(hour,2)
                    loggedTime = loggedTime + hour
                    print(loggedTime)
                else:
                    loggedTechCatergories[currentTechCategory] = hour

                if loggedTime == totalTime:
                    print("Thanks for logging")
                    print(loggedTechCatergories)
                    break
                
                print(loggedTechCatergories)
            return loggedTechCatergories
        else:
            return loggedTechCatergories
            
    except Exception as identifier:
        print(identifier)

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
                dataframe.to_csv("tables/time_sheet_master.csv",index = False)

            else:
                if not pd.isna(dataframe['learning'].iloc[dataframe.shape[0]-1]):
                    loggedCategories['learning'] = dataframe['learning'].iloc[dataframe.shape[0]-1]
                if not pd.isna(dataframe['work'].iloc[dataframe.shape[0]-1]):
                    loggedCategories['work'] = dataframe['work'].iloc[dataframe.shape[0]-1]
            print(dataframe.tail())

            if "learning" in loggedCategories or 'work' in loggedCategories:
                learntInwork = 0.0
                timeLoggedInLearning = 0.0
                if 'work' in loggedCategories:
                    learntInWork = float(input("Enter the amount of hours you learnt during work (Time logged in work - {} )- ".format(loggedCategories['work'])))
                learningDf = pd.read_csv('tables/learning_time_sheet.csv')
                if 'learning' in loggedCategories:
                    timeLoggedInLearning = loggedCategories['learning']
                totalTime = learntInWork + timeLoggedInLearning
                techCategories = learningDf.columns
                loggedTechCategories = logLearningTimeSheet(techCategories,totalTime)
                if bool(loggedTechCategories):
                    learningDf = learningDf.append(loggedTechCategories,ignore_index=True)
                    learningDf.to_csv("tables/learning_time_sheet.csv",index = False)
                else:
                    if not pd.isna(learningDf['python'].iloc[learningDf.shape[0]-1]):
                        loggedTechCategories['python'] = learningDf['python'].iloc[learningDf.shape[0]-1]
                print(learningDf.tail())
            
            if "python" in loggedTechCategories:
                pythonDf = pd.read_csv('tables/python_time_sheet.csv')
                pyModules = pythonDf.columns
                pyTimeLogged = loggedTechCategories['python']
                loggedPyModules = logPyTimeSheet(pyModules, pyTimeLogged)
                if bool(loggedPyModules):
                    pythonDf = pythonDf.append(loggedPyModules,ignore_index=True)
                    pythonDf.to_csv("tables/python_time_sheet.csv",index = False)
                print(pythonDf.tail())

            mindsetDf = pd.read_csv('tables/mindset_analyser.csv')
            mindsetCategories = mindsetDf.columns
            ratedCategories = analyseMindSet(mindsetCategories)
            if bool(ratedCategories):
                mindsetDf = mindsetDf.append(ratedCategories,ignore_index=True)
                mindsetDf.to_csv("tables/mindset_analyser.csv",index = False)
            print(mindsetDf.tail())


        if userInput == 2:
            userChoice = input("""
            1. Time spent on each day in particular category
            2. Time spent on last logged day in each category
            """)
            if userChoice == "1":
                [print("{} {}".format(ind+1,val)) for ind,val in enumerate(categories[2:-1])]
                select = int(input("Select the category!!"))
                currentCategory = categories[select+1]
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


    