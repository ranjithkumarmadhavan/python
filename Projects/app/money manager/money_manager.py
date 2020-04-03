import json

accountDetails = open("balance.json")
balance = json.load(accountDetails)

auth = """
1. Already user
2. Sign up
"""

authInput= input()

if authInput == "1":
    userName = input("Enter userName : ")
    passWord = input("Enter password : ")

options = """
Please select a option.
1.View balance
2.Add expense
3.Add income
4.Exit
"""

while True:
    print(options)

    userInput = input()
    if userInput == "1":
        print('Your current balance is {}.{}'.format(balance['currency'],balance['balance']))

    elif userInput == "2":
        exp = input("Enter the amount : ")
        balance["balance"] = float(balance["balance"]) - int(exp)
        print(balance)
        with open("balance.json","w") as output:
            json.dump(balance,output)
    elif userInput == "3":
        exp = input("Enter the amount : ")
        balance["balance"] = float(balance["balance"]) + int(exp)
        print(balance)
        with open("balance.json","w") as output:
            json.dump(balance,output)
    elif userInput == "4":
        break;

