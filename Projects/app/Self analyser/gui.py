from tkinter import *
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import selfAnalyserUtil


def ok():
    print("value is ",variable.get())

def showStatistics():
    print("Selected value : ",default.get())
    select = options.index(default.get())
    print(select)
    currentCategory = categories[select+2]
    plt.bar(dataframe.date,dataframe[currentCategory])
    plt.xticks(rotation=45)
    plt.xlabel("date")
    plt.ylabel("time spent on {} in hours".format(currentCategory))
    plt.title("Time spent on {} each day".format(currentCategory))
    plt.show()

def logTimeSheet():
    screen1 = Toplevel(screen)
    screen1.title("Log Time Sheet")
    screen1.geometry("300x250")

    global variable
    variable = StringVar(screen1)
    variable.set("one") # default value

    OptionMenu(screen1,variable,"test1","test2","test3").pack()
    button = Button(screen1,text = "Ok",command = ok).pack()

def viewStatistics():
    global dataframe
    dataframe = pd.read_csv("tables/time_sheet_master.csv")
    global categories
    categories = dataframe.columns

    screen2 = Toplevel(screen)
    screen2.title("View Statistics")
    screen2.geometry("300x250")

    global options
    options = ["{}".format(val) for ind,val in enumerate(categories[2:-1])]
    print(options)
    global default
    default = StringVar(screen2)
    default.set(options[0])
    OptionMenu(screen2,default,*options).pack()
    button = Button(screen2,text = "Ok",command = showStatistics).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Self Analyser")
    Label(text = "Self Analyser",bg = "grey",width="300",height="2",font=("Calibri",13)).pack()
    Label(text = " ").pack()
    Button(text = "Log Time Sheet",height = "2",width = "30",command = logTimeSheet).pack()
    Label(text = " ").pack()
    Button(text = "View Statistics",height = "2",width = "30",command = viewStatistics).pack()
    Label(text = " ").pack()
    Button(text = "Exit",height = "2",width = "30",command = screen.destroy).pack()
    
    screen.mainloop()

main_screen()