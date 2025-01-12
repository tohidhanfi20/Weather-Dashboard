import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def fetch_weather(api_key, city):
    """Fetch weather data from OpenWeather API"""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }

    if not api_key:
        raise ValueError("API Key is missing. Ensure OPENWEATHER_API_KEY is set in the environment.")

    try:
        print(f"Requesting URL: {base_url} with params: {params}")
        response = requests.get(base_url, params=params)
        print(f"Response Status Code: {response.status_code}")
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Test the function
if __name__ == "__main__":
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    CITY = "Nagpur"  # Replace with the city you want to test

    print(f"Testing weather fetch for {CITY}...")
    weather_data = fetch_weather(API_KEY, CITY)

    if weather_data:
        print(f"Weather Data for {CITY}:")
        print(weather_data)
    else:
        print(f"Failed to fetch weather data for {CITY}")