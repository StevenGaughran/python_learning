import requests
from datetime import datetime

# Setup for time and date
date = datetime.now()
today = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")

# Nutritionix HTTP Post pull
nutritionix_headers = {
    "x-app-id": "yes",
    "x-app-key": "alsoyes"
}

query = input("Tell me what kind of exercise you did: ")

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_exercise_endpoint_params = {
    "query": query,
    "gender": "male",
    "weight_kg": 64,
    "height_cm": 175,
    "age": 39

}

nutritionix_response = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_exercise_endpoint_params,
                                     headers=nutritionix_headers)
nutritionix_result = nutritionix_response.json()

nutritionix_data = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": nutritionix_result["exercises"][0]["user_input"],
            "duration": nutritionix_result["exercises"][0]["duration_min"],
            "calories": nutritionix_result["exercises"][0]["nf_calories"]
                    }
}


# Sheety stuff for the Google Spreadsheet
sheety_post = "https://api.sheety.co/mindyabusiness/myWorkouts/workouts"

sheety_response = requests.post(url=sheety_post, json=nutritionix_data)
sheety_response.raise_for_status()

