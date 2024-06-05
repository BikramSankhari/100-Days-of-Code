import requests
import datetime

API_KEY = "db096bebe9d67d177bf6560853522d55"
API_ID = "7b238b4f"
time = datetime.datetime.now().strftime("%H:%M:%S")
date = datetime.datetime.now().strftime("%d/%m/%Y")

nutritionix_header = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
    "Content-Type": "application/json",
}

words = input("What exercise you did today?\n")


nutritionix_parameters = {
    "query": words,
}

nutritionix_response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                                     json=nutritionix_parameters, headers=nutritionix_header)
nutritionix_response.raise_for_status()

for item in nutritionix_response.json()["exercises"]:
    exercise_duration = item["duration_min"]
    exercise_calories = item["nf_calories"]
    exercise_name = item["name"]

    sheety_parameters = {
        "workout" : {
            "date" : str(date),
            "time" : str(time),
            "exercise" : exercise_name,
            "duration" : str(exercise_duration),
            "calories" : exercise_calories,
        }
    }

    sheety_header = {
        "Content-Type": "application/json",
    }

    sheety_response = requests.post(url="https://api.sheety.co/9e1ea077421bf0b0d8851b83bf4f0639/myWorkout/workouts", json=sheety_parameters, headers=sheety_header)
