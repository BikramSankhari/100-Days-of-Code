import requests
from datetime import date
from dateutil.relativedelta import relativedelta
import smtplib
import ssl

API_KEY = "nnSjuv2-a9euuheWjaZMNiXcqyuoh1P9"
MY_EMAIL = "popww619@gmail.com"
MY_PASSWORD = "vfyuqrhmwxtlsdwb"
HEADER = {
    "apikey": API_KEY,
}


class FlightManager:
    def __init__(self, city : str, iata_code : str, lower_price : str):
        self.city = city
        self.iata_code = iata_code
        self.lower_price = lower_price

    def get_iata_code(self):
        parameters = {
            "term": self.city,
        }

        response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=parameters, headers=HEADER)
        response.raise_for_status()
        print(response.json())
        self.iata_code = response.json()['locations'][0]['code']
        return self.iata_code

    def search_cheap_rate(self):
        today = date.today().strftime("%d/%m/%Y")
        date_to = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")

        parameters = {
            "fly_from" : "airport:CCU",
            "fly_to" : self.iata_code,
            "date_from" : today,
            "date_to" : date_to,
        }

        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=parameters, headers=HEADER)
        response.raise_for_status()

        for flight in response.json()['data']:
            if flight['price'] < self.lower_price:
                self.send_mail(departure_date= flight['route'][0]['local_departure'], price=flight['price'])
                break

    def send_mail(self, departure_date, price):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, MY_EMAIL, msg=f"Subject:CHEAP FLIGHT AVAILABLE\n\nA cheap flight for {self.city} available on {departure_date} at price {price}")