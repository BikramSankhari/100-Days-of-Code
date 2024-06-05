import requests
import re

class Sheet:
    def __init__(self):
        response = requests.get(url="https://api.sheety.co/9e1ea077421bf0b0d8851b83bf4f0639/flightDeals/prices")
        response.raise_for_status()
        self.all_data = response.json()['prices']
        self.row_count = 0
        self.city = ''
        self.iata_code = ''
        self.lowest_price = 0

        response = requests.get(url="https://api.sheety.co/9e1ea077421bf0b0d8851b83bf4f0639/flightDeals/customers")
        response.raise_for_status()
        self.customer_list = [item['email'] for item in response.json()['customers']]

    def has_more_place(self) -> bool:
        if self.row_count < len(self.all_data):
            return True
        return False

    def get_next_place(self):
        self.city = self.all_data[self.row_count]['city']
        self.iata_code = self.all_data[self.row_count]['iataCode']
        self.lowest_price = self.all_data[self.row_count]['lowestPrice']
        self.row_count += 1

    def update_iata_code(self):
        parameters = {
            'price' : {
                "iataCode" : self.iata_code,
            }
        }
        response = requests.put(url=f"https://api.sheety.co/9e1ea077421bf0b0d8851b83bf4f0639/flightDeals/prices/{self.row_count + 1}", json=parameters)
        response.raise_for_status()

    def add_new_customer(self):
        name = input("Enter Your Full Name: ")
        while True:
            email = input("Enter Your Email Address ")
            if re.fullmatch("[A-Za-z0-9]+@[a-z]+(.[a-z]+){1,2}", email):
                break
            else:
                print("Invalid Email Address. Please Try Again")

        parameters = {
            "customer" : {
                "name" : name,
                "email" : email,
            }
        }

        response = requests.post(url="https://api.sheety.co/9e1ea077421bf0b0d8851b83bf4f0639/flightDeals/customers", json=parameters)
        self.customer_list.append(email)