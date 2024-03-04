import pandas
import os
from account_creator import Account
#-------------------------------------------------------------------------------------------
#                         RodriBank Financial Services and Bank
account = Account()

app_is_on = True

while app_is_on:
    choice = input("What would you like to access?\nCreate Account or Access Account\nLeave Site: ").lower()
    os.system("cls")
    if choice == "create account" or choice == "create":
        account.create_account()
    elif choice == "access account" or choice == "access":
        account.access_account()
    elif choice == "leave site":
        os.system("cls")
        print("We thank you for using RodriBank Financial Services")
        break
    else:
        print("Something went wrong. Try again.")
#--------------------------------------------------------------------------------------------
