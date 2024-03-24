import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 25.032969
MY_LONG = 121.565414

email = "yentingliu905@gmail.com"
password = "12345678"



def is_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def night_time():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().time().hour
    if not sunrise < time_now < sunset:
        return True


# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_over_head() and night_time():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email,password)
        connection.sendmail(from_addr= email,
                            to_addrs= email,
                            msg= "Subject:Look up 👆\n\nThe ISS is above you in the sky."
                            )
