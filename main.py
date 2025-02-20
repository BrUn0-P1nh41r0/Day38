import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

##API info
APP_ID = os.environ["NUTRITION_APP_ID"]
API_KEY = os.environ["NUTRITION_API_KEY"]
USERNAME = os.environ["SHEETY_USERNAME"]
PASSWORD = os.environ["SHEETY_PASSWORD"]

##API parameters
GENDER = "Male"
WEIGHT_KG = 110
HEIGHT_CM = 174
AGE = 23

##API Endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["SHEETY_ENDPOINT"]

##Sheety API Basic Auth
basic = HTTPBasicAuth(USERNAME, PASSWORD)

##Date
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#Input for API
exercise_text = input("Tell me which exercises you did: ")

##API Header
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

##API Parameters
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint,json=sheet_inputs,auth=basic)
    print(sheet_response.text)


