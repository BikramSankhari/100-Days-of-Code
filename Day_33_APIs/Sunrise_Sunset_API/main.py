import requests
import time
from datetime import datetime
MY_LAT = 17.700180
MY_LONG = 83.287659

parameters = {
    'lat' : MY_LAT,
    'lng' : MY_LONG,
}

response = requests.get(url="https://api.sunrisesunset.io/json", params=parameters)

sunset_time = response.json()['results']['sunset']
sunset_time = datetime.strptime(sunset_time, "%I:%M:%S %p")
print(f"Sunset time : {sunset_time}")


now = datetime.now()
now = datetime.strftime(now, "%I:%M:%S %p")
now = datetime.strptime(now, "%I:%M:%S %p")


