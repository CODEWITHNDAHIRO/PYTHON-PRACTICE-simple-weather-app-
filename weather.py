import json 
import urllib.request 
# 1. Defining the API endpoint with coordinates ( my home/Duisburg/latitude/longitude)
#open-Meteo requires no API key, making it ideal for learning.
LATITUDE = 51.4344
LONGITUDE = 6.7623
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current=temperature_2m,wind_speed_10m"

def fetch_weather():
    print(f"Connecting to Open-Meteo API for coordinates({LATITUDE},{LONGITUDE})...")

    try:

        with urllib.request.urlopen(API_URL) as response:
            data = response.read() .decode('utf-8')

            weather_data=json.loads(data)
            return weather_data
    except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None
if __name__ == "__main__":
    result = fetch_weather()
    if result:
        print("\nRaw JSON response received successfully:")
        print(json.dumps(result, indent=4))
