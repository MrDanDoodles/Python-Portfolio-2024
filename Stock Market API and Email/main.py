STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

from datetime import datetime, timedelta
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#-------------------------------------------------------------------------------------------

#           --TimeStamp--
time_call = datetime.now()
#   Today
today_stamp = time_call.strftime("%Y-%m-%d")
#Yesterday
yesterday = time_call - timedelta(days=1)
yesterday_stamp = yesterday.strftime("%Y-%m-%d")

#-------------------------------------------------------------------------------------------

#           --Stock API and Data--
API_KEY = "HFHFHFHFHFHFH5643"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

#   Accessing Data
stock_api = requests.get(url=STOCK_ENDPOINT, params=parameters)
stock_api.raise_for_status()
stock_data = stock_api.json()
#   Today 
open_stock = float(stock_data["Time Series (Daily)"][today_stamp]["1. open"])
close_stock = float(stock_data["Time Series (Daily)"][today_stamp]["4. close"])
#Difference of Open and Close
today_difference = abs(round(open_stock - close_stock, 2))

#   Yesterday
yesterday_close_stock = float(stock_data["Time Series (Daily)"][yesterday_stamp]["4. close"])

#   Finding Percentage Difference
percentage_dif = round(((yesterday_close_stock - close_stock) / close_stock * 100), 2)
print(f"{percentage_dif}%")

#-------------------------------------------------------------------------------------------

#           --News Data and Final Message--
news_API_KEY = "HFHFHFHFHHGHGHGH23"

news_paramaters = {
    "apiKey": news_API_KEY,
    "q": COMPANY_NAME,
    "from": yesterday_stamp,
    "to": today_stamp,
    "language": "en",
}

news_api = requests.get(url=NEWS_ENDPOINT, params=news_paramaters)
news_api.raise_for_status()

news_data = news_api.json()

article_1 = f"Title:{news_data['articles'][0]['title']}\n\nDescription:{news_data['articles'][0]['description']}\n\nLink:{news_data['articles'][0]['url']}"
article_2 = f"Title:{news_data['articles'][1]['title']}\n\nDescription:{news_data['articles'][1]['description']}\n\nLink:{news_data['articles'][1]['url']}"
article_3 = f"Title:{news_data['articles'][2]['title']}\n\nDescription:{news_data['articles'][2]['description']}\n\nLink:{news_data['articles'][2]['url']}"

articles_formatted = f"------\n{article_1}\n-------\n{article_2}\n-------\n{article_3}"

final_message = f"""
Hello Danielle,\n
Today TSLA has a {percentage_dif}% percent difference from the previous day.\n
TSLA opened at ${open_stock} and closed at ${close_stock} with a ${today_difference} difference.\n
Here is some information gathered from the news as to why TSLA's stock value may have fluctuated:\n
{articles_formatted}
"""

#-------------------------------------------------------------------------------------------
#           ----Sending the Final Message via Email----
my_email = "test@gmail.com"
password = "jnaflnrkjnatestfake"
recipient_email = "someone@gmail.com"

subject = f"TSLA Stock {today_stamp}"
body = f"{final_message}"

msg = MIMEMultipart()
msg['From'] = my_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain', 'utf-8'))

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=recipient_email,
                        msg=msg.as_string())

#-------------------------------------------------------------------------------------------