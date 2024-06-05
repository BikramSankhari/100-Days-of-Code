import time
import requests
import smtplib
import ssl

MY_LAT = 17.700180
MY_LONG = 83.287659
MY_EMAIL = "popww619@gmail.com"
MY_PASSWORD = "wftzytgpbgvaledj"


def send_mail():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mail:
        mail.login(MY_EMAIL, MY_PASSWORD)
        mail.sendmail(MY_EMAIL, 'bikram1209@gmail.com', msg="Subject:ISS OVERHEAD\n\nLOOK UP")


parameters = {
    'lat' : MY_LAT,
    'lng' : MY_LONG,
}

while True:
    response_of_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_of_iss.raise_for_status()
    iss_longitude = float(response_of_iss.json()["iss_position"]["longitude"])
    iss_latitude = float(response_of_iss.json()["iss_position"]["latitude"])

    print(f"Latitude: {iss_latitude}, longitude:{iss_longitude}")
    if (iss_latitude - 5 <= MY_LAT <= iss_latitude + 5) and (iss_longitude - 5 <= MY_LONG <=
                                                                                   iss_longitude + 5):
        send_mail()
        break

    time.sleep(60)
