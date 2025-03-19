import requests 
import os
from datetime import datetime 

NUTRITION_API_KEY = os.environ("NUTRITION_APP_ID")
NUTRITION_APP_ID = os.environ("NUTRITION_APP_ID")
EXERCISE_URL = os.environ("EXERCISE_URL")

headers = {
    'x-app-id': NUTRITION_APP_ID,
    'x-app-key': NUTRITION_API_KEY
}

GENDER = "male"
WEIGHT_KG = 110
HEIGHT_CM = 220
AGE = 90

params = {
    "query": '',
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

def get_user_input():
    user_response = input("What exercise did you do?: ")
    return user_response

def process_exercise(user_response):
    params["query"] = user_response
    try: 
        response = requests.post(url=EXERCISE_URL, headers=headers, json=params)
    except ConnectionRefusedError:
        print("Connection Refused")
    else:
        return response.json

def update_google_sheet(results, today, now):
    GOOGLE_SHEET_NAME = "workout"
    sheet_endpoint = os.environ["SHEETY_ENDPOINT"]

    
    for exercise in results["exercises"]:
        sheet_inputs = {
            GOOGLE_SHEET_NAME: {
                "date": today,
                "time": now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        try:
            sheet_response = requests.post(
            sheet_endpoint,
            json=sheet_inputs,
            auth=(
                os.environ["ENV_SHEETY_USERNAME"],
                os.environ["ENV_SHEETY_PASSWORD"],
                )
            )
        except:
            print("Could not post data to Google Sheets")

        else:
            print(f"Response: {sheet_response.text}")


user_response = get_user_input()

results = process_exercise(user_response)

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

update_google_sheet(results, today, now)