import requests
from datetime import datetime
import smtplib

MY_LAT = 30.325970 
MY_LONG = -81.656761

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/Havana"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

#-------Functions-------
#   0 = no | 1 = yes
#Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():
    if (MY_LAT + 5) >= iss_latitude and (MY_LAT - 5) <= iss_latitude and (MY_LONG + 5) >= iss_longitude and (MY_LONG - 5) <= iss_longitude:
        return 1
    else:
        return 0
#If it is dark out
def is_dark():
    if hour <= sunrise or hour <= sunset:
        return 1
    else:
        return 0
    
def lookup():
    if iss_nearby() == 1 and is_dark() == 1:
        message = "Subject:ISS Overhead\n\nCongrats Danielle, the ISS should be near you. You should look up in the night sky!"
        my_email = "danielletesting0@gmail.com"
        my_password = "fmizoiflxhhopziz"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="1211danielle@gmail.com", msg=message)
    else:
        print("False")

lookup()



