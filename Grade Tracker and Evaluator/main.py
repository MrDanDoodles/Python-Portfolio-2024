from account_actions import TimeStamp, AccountAction
#------App------

print("Thank you for choosing Grade Tracker from RodriTech")

#Timestamp in the Background Working
TimeStamp.current_time
ac = AccountAction()

app_on = True
while app_on:
    selection = input("Create Account (CA) or Login (L): ").upper()
    if selection == "CA":
        ac.account_create()
    elif selection == "L":
        ac.account_access()
    elif selection != "CA" or selection != "L":
        print("Please type in the correct input")