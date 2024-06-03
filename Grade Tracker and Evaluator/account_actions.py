#This file is where the classes for the functions will be
import json
import datetime as dt
import os
import smtplib

class TimeStamp:
    current_time = dt.datetime.now()
    minute = current_time.minute
    hour = current_time.hour
    day = current_time.day
    month = current_time.month
    year = current_time.year

    time_stamp = f"{hour}:{minute} | {month}/{day}/{year}"


class AccountAction:

    def __init__(self):
        self.account_dictionary = {
            "account info": {
                "username": [],
                "password": [],
                "email": [],
            },
            "class info": {
                "class": [],
                "grade": [],
            },
            "averages info": {
                "average": [],
                "timestamp": [],
            }
        }

    def account_create(self):
        #Create the Username and Password
        username = str(input("Username: ")).lower()
        password = str(input("Password: "))
        email = str(input("Email: "))
        self.account_dictionary["account info"]["username"].append(username)
        self.account_dictionary["account info"]["password"].append(password)
        self.account_dictionary["account info"]["email"].append(email)
        os.system("cls")
        #Create a dictionary of classes
        new_classes = True
        while new_classes:
            new_class = input("Do you have a class you would like to list? Yes or No: ").lower()
            if new_class == "yes":
                os.system("cls")
                class_name = str(input("what is the name of the class?: ").lower())
                cg_check = input(f"Does {class_name} have a grade you would like to save? Yes or No: ").lower()
                cg_num = 1
                while cg_num == 1:
                    if cg_check == "yes":
                        class_grade = float(input(f"What is your grade in {class_name}: "))
                        cg_num -= 1
                    elif cg_check == "no":
                        class_grade = float(0)
                        cg_num -= 1
                    else:
                        print("You must type Yes or No")
                    self.account_dictionary["class info"]["class"].append(class_name)
                    self.account_dictionary["class info"]["grade"].append(class_grade)
            elif new_class == "no":
                new_classes = False
            elif new_class != "no" or new_class != "yes":
                os.system("cls")
                print("That is not an acceptable answer. Please type Yes or No")
        
        #Create the First Average for the grades with a Time Stamp
        total_sum = 0
        for index in self.account_dictionary["class info"]["grade"]:
            total_sum += index
        average = round(total_sum / len(self.account_dictionary["class info"]["grade"]), 2)
        self.account_dictionary["averages info"]["average"].append(average)
        self.account_dictionary["averages info"]["timestamp"].append(TimeStamp.time_stamp)

        #Create the JSON file
        with open(f"Python\\Personal Projects\\GPA Evaluator\\Account Folders\\{username}.json", "w") as data_file:
            json.dump(self.account_dictionary, data_file, indent=4)

        #Send an email stating that your account was created
        c_email = "testing@gmail.com"
        c_password = "jsjsjsjsjsjsjssjsjs"

        message = f"Subject:GPA Calculator Account\n\nThank you {username} for signing up for the GPA Calculator and Grade Tracker.\nYour account was created on {TimeStamp.time_stamp}. We hope to serve you well, your current grade average is {average}. Hope you can keep up the work!"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=c_email, password=c_password)
            connection.sendmail(from_addr=c_email, to_addrs=email, msg=message)

    def account_access(self):
    #Login Process
        app_is_on = True
        while app_is_on:
            username = input("Username: ").lower()
            password = input("Password: ")
            os.system("cls")

            try:
                with open(f"Python\\Personal Projects\\GPA Evaluator\\Account Folders\\{username}.json", "r") as data_file:
                    account_data = json.load(data_file)
                
                if password == account_data["account info"]["password"][0]:
                    pswrd_correct = True
                    while pswrd_correct:
                        choice = input("What would you like to do? View Grades and Average (VGA) or Update Grades (UG) or Logout: ").upper()

                        #Viewing Grades
                        if choice == "VGA":
                            for index in range(len(account_data["class info"]["class"])):
                                print(f"Class: {account_data['class info']['class'][index]} | Grade: {account_data['class info']['grade'][index]}")
                            print(f"Grade Average: {account_data['averages info']['average'][0]}")


                        #Updating Grades
                        elif choice == "UG":
                            os.system("cls")
                            #File Opened
                            with open(f"Python\\Personal Projects\\GPA Evaluator\\Account Folders\\{username}.json", "r") as data:
                                updated_data = json.load(data)

                            #Selecting Option
                            choice2 = input("What would you like to update?\nAn existing grade or add a new class (EC)\nAdd a class (AC)\n").upper()
                            #------Updating------
                            #Existing Class
                            if choice2 == "EC":
                                for index in updated_data["class info"]["class"]:
                                    print(index)
                            #Selecting the Class
                            #Updating Selected Class via the Index
                                class_select = True
                                while class_select:
                                    try:
                                        class_selection = input("which class would you like to update: ")
                                        grade_index = updated_data["class info"]["class"].index(class_selection)
                                        print(updated_data["class info"]["grade"][grade_index])
                                        class_select = False
                                    except ValueError:
                                        print("Class was not found, please type in a new class")
                                grade_update = True
                                while grade_update:
                                    try:
                                        new_grade = float(input("What will the new grade be?: "))
                                        grade_update = False
                                    except ValueError:
                                        print("Please type a number, not a letter.")
                                updated_data["class info"]["grade"][grade_index] = new_grade
                            

                            #------Appending------
                            elif choice2 == "AC":
                                os.system("cls")
                                #Opening the File
                                with open(f"Python\\Personal Projects\\GPA Evaluator\\Account Folders\\{username}.json", "r") as data:
                                    updated_data = json.load(data)
                                adding_classes = True
                                #Looping until the user is done.
                                while adding_classes:
                                    class_addition = input("What class would you like to add?: ").lower()

                                    adding_grade = True
                                    while adding_grade:
                                        try:
                                            grade_addition = float(input(f"What is the current grade for {class_addition}?: "))
                                            adding_grade = False
                                        except ValueError:
                                            print("Please type in a number")
                                            
                                    updated_data["class info"]["class"].append(class_addition)
                                    updated_data["class info"]["grade"].append(grade_addition)
                                    adding_classes_check = input("Would you like to add another class? Yes or No:").lower()
                                    #Checking to see if User wants to stop adding classes
                                    if adding_classes_check != "yes":
                                        adding_classes = False
                                        print("To view any changes. The application needs to be restarted.")
                                
                            #------Updating the JSON File------
                            #Creating the average
                            total_sum = 0
                            for index in updated_data["class info"]["grade"]:
                                total_sum += index
                            average = round(total_sum / len(updated_data["class info"]["grade"]), 2)
                            updated_data["averages info"]["average"][0] = average
                            updated_data["averages info"]["timestamp"][0] = TimeStamp.time_stamp

                            with open(f"Python\\Personal Projects\\GPA Evaluator\\Account Folders\\{username}.json", "w") as data:
                                json.dump(updated_data, data, indent=4)


                        #Logging Out
                        elif choice == "LOGOUT":
                            print("Thank you for stopping by!")
                            app_is_on = False
                            break
                else:
                    print("Please Try Again")
            except FileNotFoundError:
                print("That account was not found. Please Try Again")
