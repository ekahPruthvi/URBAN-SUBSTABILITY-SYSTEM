import requests
import Location
API_KEY = "enterkeyhere"

# Location
lat, long, city, state, country = Location.locationCoordinates()

if(country == "IN"):
    country = "India"
elif(country != "IN"):
    print("Not supported")

print(lat, long, city, state, country)

# IQAir API URL
url = f"https://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={API_KEY}"

# Fetch Data
response = requests.get(url)
def get_AQI():
    if response.status_code == 200:
        data = response.json()
        
        # Extract AQI Data
        if "data" in data and "current" in data["data"]:
            aqi = data["data"]["current"]["pollution"]["aqius"]  # AQI in US standard
            return aqi
        else:
            print("No AQI data found.")
            return 0
    else:
        print(f"Error {response.status_code}: {response.text}")