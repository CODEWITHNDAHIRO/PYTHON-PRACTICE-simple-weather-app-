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

def parse_weather(weather_data):
     """Extracts and formats specific metrics from the raw JSON dictionary."""

     current = weather_data.get ("current",{}) #extracting nested dictionaries safely using .get()
     units = weather_data.get("current_units",{}) 

     temperature = current.get("temperature_2m")
     temp_unit =  weather_data.get("temperature_2m","°C") # Pull out specific data points and their units 

     wind_speed = current.get("wind_speed_10m")
     wind_unit =units.get("wind_speed_10m", "km/h")

     observation_time = current.get("time")

     # Printing a clean human-readable report
     print("\n" + "="*40)
     print(f" 🌦️  CURRENT WEATHER REPORT (Duisburg)")
     print("="*40)
     print(f"Observation Time: {observation_time}")
     print(f"Temperature: {temperature} {temp_unit}")
     print(f"Wind Speed: {wind_speed} {wind_unit}")
     print("="*40)
if __name__ == "__main__":
    result = fetch_weather()
    if result:
       parse_weather(result)