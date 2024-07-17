#                           The Ebay Tracker
#   ----Imports----
from account import Account_
from webscraper import Webscraper
import json
#-------------------
ac = Account_()
account = ac.access_account()

wb = Webscraper()
new_data = wb.link_scrapper(link_check=wb.link_checker(wb.link) , account=account)

with open(f"Python\\Personal Projects\\Item Tracker\\accounts\\{account}.json", "w") as file:
    json.dump(new_data, file, indent=4)
