#%%
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
nutrition_id = os.getenv('NUTRITION_ID')
nutrition_key = os.getenv('NUTRITION_KEY')

NUTRITION_HOST = 'https://trackapi.nutritionix.com'
NUTRITION_ENDPOINT = '/v2/natural/exercise'


exercise = input('Tell me which exercise you did: ')
user_params = {'query':exercise,
               'weight_kg':82,
               'height_cm':177,
               'age':26}

headers = {
    "x-app-id": nutrition_id,
    "x-app-key": nutrition_key 
}

nutrition_exercise_endpoint = f"{NUTRITION_HOST}/{NUTRITION_ENDPOINT}"

response = requests.post(url=nutrition_exercise_endpoint, json=user_params, headers=headers)
print(response.json())

# %%
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_url = os.getenv('SHEETY_URL')
headers = {'Authorization': f'Bearer {os.getenv('BEARER_TOKEN')}'} # Bearer Token for secure authentication 
for exercise in response.json()["exercises"]:  # multiple exercises
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_url, json=sheet_inputs, headers=headers)

    print(sheet_response.text)

