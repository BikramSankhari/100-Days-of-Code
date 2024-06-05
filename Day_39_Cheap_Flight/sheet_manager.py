import requests


class Sheet:
    def __init__(self):
        response = requests.get(url="https://api.sheety.co/9e1ea077421bf0b0d8851b83bf4f0639/flightDeals/prices")
        response.raise_for_status()
        self.all_data = response.json()['prices']
        self.row_count = 0
        self.city = ''
        self.iata_code = ''
        self.lowest_price = 0

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
