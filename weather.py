import json 
import urllib.request 
# 1. store a dictionary  of the present cities with their coordinates 
CITIES ={
     "duisburg": {"latitude": 51.4344, "longitude": 6.7623},
     "berlin": {"latitude": 52.5200, "longitude": 13.4050},
     "kigali": {"latitude": -1.9706, "longitude": 30.1044}
    
 }
 
def fetch_weather(city_name,latitude,longitude):
    print(f"\nConnecting to Open-Meteo API for {city_name.title()} {latitude}, {longitude}...")
     #2 injecting the dynamic latitude and longitude into our  f-string URL
    API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"

    try:

        with urllib.request.urlopen(API_URL) as response:
            data = response.read() .decode('utf-8')

            weather_data=json.loads(data)
            return weather_data
    except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None

def parse_weather(city_name,weather_data):
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
     print(f" 🌦️  CURRENT WEATHER REPORT ({city_name.upper()})")
     print("="*40)
     print(f"Observation Time: {observation_time}")
     print(f"Temperature: {temperature} {temp_unit}")
     print(f"Wind Speed: {wind_speed} {wind_unit}")
     print("="*40)
if __name__ == "__main__":
    print("Available cities: Duisburg, Berlin, Kigali")
    
    # 3. Get user input, clean it up with .strip().lower()
    user_input = input("Enter a city name: ").strip().lower()
    
    # 4. Validate if the city exists in our dictionary
    if user_input in CITIES:
        coords = CITIES[user_input]
        result = fetch_weather(user_input, coords["latitude"], coords["longitude"])
        if result:
            parse_weather(user_input, result)
    else:
        print(f"Sorry, '{user_input}' is not in our database yet. Try running the script again!")