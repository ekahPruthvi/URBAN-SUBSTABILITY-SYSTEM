import requests
import folium
    # return coordinates using device ip address

def locationCoordinates():
    try:
              
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        country = data.get('country', 'Unknown')
        return lat, long, city, state, country
    except:
        # Displaying ther error message
        print("Internet Not avialable")
        exit()
        return False


# this method will fetch our coordinates and create a html file
# of the map
def gps_locator():

    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state, country  = locationCoordinates()
        print("Location Pointed to {},{},{}\n".format(city, state, country))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)
        return city
    except:
        return False

