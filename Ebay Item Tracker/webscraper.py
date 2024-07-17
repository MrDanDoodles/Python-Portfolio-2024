#       ----Item Tracker----
#--------------------
#   --Imports--
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
#--------------------
class Webscraper:
#   --Account--

    def __init__(self):
        #   --Variables and Dicts----
        self.link = input("Link: ")
        self.shopping_cart = {
            "Ebay": [{}]
        }

        self.driver = webdriver.Chrome()
    #   --Functions--
    def link_checker(self, link):
        checking = True
        while checking:
            if "ebay" in link:
                checking = False
                return("Ebay")
            elif "amazon" in link:
                print("Amazon is not a supported platform for this App. Please input an Ebay Link")
            else:
                print("The link you gave us does not work. Please input an Ebay link.")

    def link_scrapper(self, link_check, account):
        with open(f"Python\\Personal Projects\\Item Tracker\\accounts\\{account}.json", "r") as data:
            self.account_data = json.load(data)

        self.link
        self.shopping_cart

        index = len(self.account_data["Ebay"]) + 1

        info_dump = {
            f"item_{index}": {
                "Name": "",
                "Price": "",
                "Link": ""
            }
        }
        if link_check == "Ebay":
            #   Collecting Data
            self.driver.get(self.link)
            name = self.driver.find_element(By.TAG_NAME, "h1")
            price = self.driver.find_element(By.CSS_SELECTOR, ".x-price-primary .ux-textspans")
            #   Formatting Data
            format_name = name.text
            format_price = int(re.sub("[^0-9]","",price.text)) / 100
            info_dump[f"item_{index}"]["Name"] = format_name
            info_dump[f"item_{index}"]["Price"] = format_price
            info_dump[f"item_{index}"]["Link"] = self.link
            #   Appending Data
            self.account_data["Ebay"].update(info_dump)
            self.driver.quit()
            
            return self.account_data
