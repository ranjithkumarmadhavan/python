import pandas as pd
from datetime import datetime
import matplotlib

dataframe = pd.read_csv("time_sheet.csv")

# print(df.head())
print("Self Assessment")

def fill24Hours(categories):
    totalTime = 24
    loggedTime = 0
    loggedCategories = {}
    currentDate = str(datetime.now().date())
    wakeUpTime = input("Enter the time you woke up today (in 6:00A.M. format) : ")
    loggedCategories['date'] = currentDate
    loggedCategories['wakeup time'] = wakeUpTime

    while True:
        [print("{} {}".format(ind+1,val)) for ind,val in enumerate(categories[2:-1])]
        select = int(input("Log your 24 hours under these categories!! -- Remaining time : {}\n".format(totalTime-loggedTime)))
        hour = int(input("Enter the time spent in {}".format(categories[select+1])))
        print(loggedCategories)
        if categories[select+1] not in loggedCategories:
            print("if")
            loggedCategories[categories[select+1]] = hour
            loggedTime = loggedTime + hour
            print(loggedTime)
        else:
            print("else")
            loggedCategories[categories[select+1]] = hour

        if loggedTime == totalTime:
            bedTime = input("Enter the time you went to bed today (in 11:00P.M. format) : ")
            loggedCategories['time to bed'] = bedTime
            print("Thanks for logging")
            print(loggedCategories)
            break
        
    return loggedCategories


userInput = int(input(("""
###################################
1.Log time sheet
2.View Statistics
Enter your choice: """)))

shape = dataframe.shape

if userInput == 1:
    categories = dataframe.columns
    loggedCategories = fill24Hours(categories)
    dataframe = dataframe.append(loggedCategories,ignore_index=True)

print(dataframe.head())

dataframe.to_csv("time_sheet.csv",index = False)