import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

my_email = "EyeHeartNickelback@gmail.com"
password = "12345"


def lat_close_enough():
    if iss_latitude in range(27, 37):
        return True


def long_close_enough():
    if iss_longitude in range(-112, 122):
        return True


def is_it_dark():
    if sunset < hour < sunrise:
        return True


def ship_it(lat, long, dark):
    time.sleep(60)
    if lat and long and dark == True:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="Ih8Nickelback@yahoo.com",
                msg=f"Subject:Monday Motivation!\n\nHello!\nThe ISS is currently overhead!"
            )


ship_it(lat_close_enough(), long_close_enough(), is_it_dark())
