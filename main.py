import requests
import datetime as dt
APP_ID = "YOUR NTFE KEY"
API_KEY = "YOUR SHEETY API KEY"

NTFE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/5fad7be647263491912fc2d2563329fd/workoutTracking/workouts"

headers={
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key':API_KEY,
    
}
user_input = input("Tell me what exercise you did:")
user_params = {
    "query":user_input
}


response = requests.post(url=NTFE_ENDPOINT,headers=headers,json=user_params)
daily_data = response.json()["exercises"][0]
today = dt.datetime.now()
day = str(today.strftime("%d/%m/%Y"))
time = str(today.now().time()).split(".")[0]
exercice = str(daily_data["user_input"].title())
informations = {
    "workout" : {
        "date":day,
        "time":time,
        "exercise":exercice,
        "duration":daily_data["duration_min"],
        "calories":daily_data["nf_calories"],

    }
  }
# chose the basic authentification
sheety_headers ={
    "Authorization":"YOUR BASIC AUTHENTIFY KEY"
} 

sheety_response = requests.post(url=SHEETY_ENDPOINT,json=informations,headers=sheety_headers)

print(sheety_response.text)