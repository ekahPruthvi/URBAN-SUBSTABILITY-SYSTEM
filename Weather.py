import requests
import Location
#from Location import locationCoordinates, gps_locator
key = "244651ed82aa541a525c46cd5fd87a13"
def get_location():
    
    try:
        # Get user's location          
        x = Location.locationCoordinates()
        lat = x[0]
        long = x[1]
        return lat, long
    except:
        print("Couldn't get location")
get_location()

def get_weather():
    lat, long = get_location()
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=metric&appid={key}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city = data.get("name", "Unknown Location")
            country = data["sys"]["country"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_description = data["weather"][0]["description"]

            print(f"Temperature: {temperature}°C")
            print(f"Weather: {weather_description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Error fetching weather data. Check your API key and internet connection.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        