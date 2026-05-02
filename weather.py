import requests
import os
from location import get_location

API_KEY = "a5e457260dddc1ce8e62b5ae92caade5"

def get_weather():
    city, country = get_location()

    if not city:
        city = "Banglore" # fallback
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if res.get("main"):
        temp = res["main"]["temp"]
        weather = res["weather"][0]["description"]
        humidity = res["main"]["humidity"]

        return {
            "temp": temp,
            "condition": weather,
            "humidity": humidity,
            "city": city
        }

    return None