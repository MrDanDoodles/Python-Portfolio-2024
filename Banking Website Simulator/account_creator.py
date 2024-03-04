import pandas
import os
class Account:
    
    def create_account(self):
        #User Information
        self.user_info_permanent = {
        "username": [],
        "password": [],
        "first name": [],
        "last name": [],
        "city": [],
        "age": [],
        "money": []
        }
        #Input the account information
        for every_value in self.user_info_permanent:
            self.user_info_permanent[every_value].append(input(f"Insert a new {every_value}: "))
        user_file = (self.user_info_permanent["username"][0] + ".csv")

        #Account inforation created into a txt file
        new_file = pandas.DataFrame(self.user_info_permanent)
        new_file.to_csv(f"Personal Projects\\Account Creator\\account folders\\{user_file}")
        

    def access_account(self):
        #       Access Username
        account_accessor = "Personal Projects\\Account Creator\\account folders\\" + input("Username: ") + ".csv"
        print(account_accessor)

        #       Opening Account Via Username
        account_data = pandas.read_csv(account_accessor)

        #       Password Input
        password_input = input("What is your password: ")
        os.system("cls")
        if password_input == account_data["password"][0]:
            print("Password is correct")

            #Accessing Account - LOGGED IN
            account_info_search = True
            while account_info_search == True:
                choice2 = input("What would you like to do?\nView Info\nAccount Balance\nWithdraw\nDeposit\nTransfer\nlog off\n").lower()
                
                #       Viewing Info
                if choice2 == "view info":
                    print(account_data)

                #       Account Balance
                if choice2 == "account balance":
                    print("You currently have $", account_data["money"][0])

                #       Deposit
                if choice2 == "deposit":
                    os.system("cls")
                    money_going_in = float(input("How much are you looking to deposit: "))
                    account_money = account_data["money"][0]
                    new_balance_dp = round(account_money + money_going_in, 2)
                    print(f"Your new balance is ${new_balance_dp}")
                    account_data.loc[0, ["money"]] = [new_balance_dp]
                    account_data.to_csv(account_accessor, index=False)

                #       Withdraw
                if choice2 == "withdraw":
                    os.system("cls")
                    money_coming_out = float(input("Note that deposits also come with a 10 Percent Fee\nHow much would you like to withdraw: "))
                    account_money = account_data["money"][0]
                    new_balance_wt = round(account_money - ((money_coming_out * 0.1) + money_coming_out), 2)
                    print(f"Your new balance is ${new_balance_wt}")
                    account_data.loc[0, ["money"]] = [new_balance_wt]
                    account_data.to_csv(account_accessor, index=False)

                #       Transfer
                if choice2 == "transfer":
                    account_2_accessor = "Personal Projects\\Account Creator\\account folders\\" + input("Transfer to Username: ") + ".csv"
                    account_2_data = pandas.read_csv(account_2_accessor)
                    amount = float(input("How much would you like to transfer: $"))
                    #       Transfer Process
                    transferred_money = account_data["money"][0] - amount
                    accepting_ac_money = account_2_data["money"][0] + amount
                    #       Dictionary 1
                    account_data.loc[0, ["money"]] = [transferred_money]
                    account_data.to_csv(account_accessor, index=False)
                    #       Dictionary 2
                    account_2_data.loc[0, ["money"]] = [accepting_ac_money]
                    account_2_data.to_csv(account_2_accessor, index=False)
                    #       Printing a successful transaction
                    print(f"Your transaction of ${amount} has been made.")
                #       Log Off
                if choice2 == "log off":
                    os.system("cls")
                    print("Thank you for using RodriBank Financial Services")
                    break
        else:
            print("Password is wrong")
#--------------------------------------------------------------
#                           TO DO
#1.) Create a transfer option to other accounts
        