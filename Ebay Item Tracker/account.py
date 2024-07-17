#       ----Account Creator----
import json
import smtplib
import random
#   --Account Setup--
class Account_:

    def __init__(self):
        self.account = {
            "Account_Info": {
                "Username": "",
                "Password": "",
                "Email": "",
                "Verification_Status": "",
                "First_Name": "",
                "Last_Name": "",
                "Gender": ""
            },
            "Ebay": {

            }
        }
    #---------------------------------------
    #   --Functions
    def create_account(self):
        #   Assigning Variables
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        gender = input("Male, Female, or other? (M, F, O): ").upper()
        username = input("Username: ").lower()
        email = input("email: ")
        password = input("Password: ")
        #   Appending the Variables
        self.account["Account_Info"]["Username"] = username
        self.account["Account_Info"]["Email"] = email
        self.account["Account_Info"]["Password"] = password
        self.account["Account_Info"]["Verification_Status"] = "Unverified"
        self.account["Account_Info"]["First_Name"] = first_name
        self.account["Account_Info"]["Last_Name"] = last_name
        self.account["Account_Info"]["Gender"] = gender
        #   Creating Account JSON File
        with open(f"Python\\Personal Projects\\Item Tracker\\accounts\\{username}.json", "w") as file:
            json.dump(self.account, file, indent=4)

    def access_account(self):
        #Entering Login and Password
        accessing_account = True
        while accessing_account:  
            try:
                username = input("Username: ").lower()
                password = input("Password: ")
                with open(f"Python\\Personal Projects\\Item Tracker\\accounts\\{username}.json", "r") as file:
                    self.account_info = json.load(file)
                if password != self.account_info["Account_Info"]["Password"]:
                    print("The password you entered is not correct.")
                else:
                    print("Account has been accessed")
                    accessing_account = False
            except FileNotFoundError:
                print("Sorry that account does not exist")

        #Checking if Account is Verified        
        verifying_account = True
        while verifying_account:
            if self.account_info["Account_Info"]["Verification_Status"] == "Unverified":
                print("Your account needs to be verified before you can perform any action.\nPlease enter the code generated that was sent to your email.")
                v_code = int(random.randint(1000, 9999))

                #   Sending Email
                bus_email = "TESTING@gmail.com"
                password = "11111111111111111"
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(user=bus_email , password=password)
                    connection.sendmail(from_addr=bus_email, 
                                        to_addrs=self.account_info["Account_Info"]["Email"], 
                                        msg=f"Subject:Account Verification\n\nThis is the code you need to verify your account:\n{v_code}")
                #   Verifying Code
                entering_code = True
                while entering_code:
                    user_code = int(input("Verification Code: "))
                    if v_code == user_code:
                        self.account_info["Account_Info"]["Verification_Status"] = "Verified"
                        with open(f"Python\\Personal Projects\\Item Tracker\\accounts\\{username}.json", "w") as file:
                            json.dump(self.account_info, file, indent=4)
                        print("Your account has been verified, you may continue.")
                        entering_code = False
                        verifying_account = False
                        return True
                    else:
                        print("The code you entered was wrong, please try again.")
            else:
                print("Account is Verified, you may proceed to the account")
                verifying_account = False
                return self.account_info["Account_Info"]["Username"]
