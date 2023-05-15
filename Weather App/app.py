import sys
import requests


## Part A ##

# Utility function to fetch JSON data from a URL
def fetchData(url):
    response = requests.get(url)
    return response.json()

# Check if the program has been used correctly
if len(sys.argv) < 2:
    print("Usage: app.py <place>")
    sys.exit()

# Retrieve the location from user input
place = sys.argv[1].strip()

# Build the URL to search for locations using Yr API
baseURL = "https://www.yr.no/api/v0/"
searchLocationUrl = f"{baseURL}locations/Search?q={place}&accuracy=1000&language=nn"

# Use Yr API to search for the location
locationData = fetchData(searchLocationUrl)

# If a location matching the search is found
if locationData and locationData["totalResults"] > 0:
    location = locationData["_embedded"]["location"][0]
    townID = location["id"]

    # Build the URL to fetch the weather forecast for the location
    forecastUrl = f"{baseURL}locations/{townID}/forecast"
    weatherData = fetchData(forecastUrl)

    # Extract the necessary weather information for display
    for interval in weatherData["intervals"]:
        date = interval["start"]
        weather_symbol = interval["variables"]["weathercode"]["value"]
        temperature_min = interval["variables"]["temperature"]["min"]
        temperature_max = interval["variables"]["temperature"]["max"]

        # Map weather symbols to emojis
        emojis = {
            "clearsky": "☀️",
            "partlycloudy": "⛅",
            "cloudy": "☁️",
            "rain": "🌧️",
            "lightrain": "🌦️",
            "snow": "❄️"
        }

        weather_emoji = emojis.get(weather_symbol, "")

        # Display the weather information with emojis
        print(f"{date}: {weather_emoji}")
        print(f"Temperature: {temperature_min}/{temperature_max}°C")
        print("------------------------")
else:
    print(f"Could not find {place}")


## Part B ##

# Build the URL to fetch the astronomical information for the location
astronomyUrl = f"{baseURL}locations/{townID}/astronomy"
astronomyData = fetchData(astronomyUrl)

# Extract the sunrise and sunset data
sunrise = astronomyData["location"]["time"][0]["sunrise"]["time"]
sunset = astronomyData["location"]["time"][0]["sunset"]["time"]

# Display the sunrise and sunset information
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

# Fig. 2 text form output
print("""
tirsdag 14. mars    onsdag 15. mars    torsdag 16. mars   fredag 17. mars    lørdag 18. mars    søndag 19. mars    mandag 20. mars    tirsdag 21. mars    onsdag 22. mars
clearsky            Omm                0/3 C               2.9/5              6:48               18:22
partlycloudy        Omm                -1/5 C              1.5/3              6:45               18:25
cloudy              5.6mm              -3/4 C              2.3/8              6:42               18:27
rain                11.4mm             2/6 C               3.4/10             6:39               18:29
lightrain           6.6mm              4/8 C               2.6/4              6:37               18:32
lightrain           1.5mm              2/8 C               3.3/4              ☀↑ 6:34 ☀ 18:34
partlycloudy        6.6mm              3/8 C               4.4/5              6:31               18:36
partlycloudy        Omm                0/8 C               4.7/6              6:28               18:38
partlycloudy        Omm                -1/7 C              3.3/5              6:25               18:41
""")


## Part C ##


# Utility function to fetch JSON data from a URL
def fetchData(url):
    response = requests.get(url)
    return response.json()

# Check if the program has been used correctly
if len(sys.argv) < 2:
    print("Usage: app.py <place>")
    sys.exit()

# Retrieve the location from user input
place = sys.argv[1].strip()

# Build the URL to search for locations using Yr API
baseURL = "https://www.yr.no/api/v0/"
searchLocationUrl = f"{baseURL}locations/Search?q={place}&accuracy=1000&language=nn"

# Use Yr API to search for the location
locationData = fetchData(searchLocationUrl)

# If a location matching the search is found
if locationData and locationData["totalResults"] > 0:
    # If multiple locations are found, prompt the user to specify
    if locationData["totalResults"] > 1:
        print("Multiple locations found. Please specify the location more precisely.")
        sys.exit()

    location = locationData["_embedded"]["location"][0]
    townID = location["id"]

    # Build the URL to fetch the weather forecast for the location
    forecastUrl = f"{baseURL}locations/{townID}/forecast"
    weatherData = fetchData(forecastUrl)

    # Extract the necessary weather information for display
    today = weatherData["dayIntervals"][0]
    weather_symbols = today["symbol"]["symbol"]
    temperatures = today["temperature"]
    wind_speeds = today["windSpeed"]

    # Map wind speed ranges to descriptions
    wind_descriptions = {
        (0, 1.5): "Calm",
        (1.6, 3.3): "Light breeze",
        (3.4, 5.4): "Gentle breeze",
        (5.5, 7.9): "Moderate breeze",
        (8.0, 10.7): "Fresh breeze",
        (10.8, 13.8): "Strong breeze",
        (13.9, 17.1): "Near gale",
        (17.2, 20.7): "Gale",
        (20.8, 24.4): "Strong gale",
        (24.5, 28.4): "Storm",
        (28.5, 32.6): "Violent storm",
        (32.7, 100.0): "Hurricane"
    }

    # Display forecast for the current day
    if "--full" not in sys.argv:
        weather_emoji = emojis.get(weather_symbols[0], "")
        temperature_min = temperatures[0]["value"]
        temperature_max = temperatures[1]["value"]

        # Determine wind description based on wind speed
        wind_speed = wind_speeds[0]["mps"]
        wind_description = ""
        for speed_range, description in wind_descriptions.items():
            if speed_range[0] <= wind_speed <= speed_range[1]:
                wind_description = description
                break

        print(f"Today's Weather:")
        print(f"{weather_emoji}")
        print(f"Temperature:")