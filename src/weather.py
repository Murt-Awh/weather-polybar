import json
import urllib.request

# The API key that you generated from openmapweather website.
apiKey="479c6fb6243dfd46346b24c6c01fa3d1"
# The city you want to get the weather for.
# I've used my own as an example.
city="manchester"
# The language you want to get the weather in.
# This should be an iso code of the language.
language="en"
# The measurement unit you want to get the weather in.
# This can metric for °C (celsius).
# imperial for °F (fahrenheit).
# and standard for K (kelvin). 
unit="metric"


# Makes a request to the API.

def makeRequest():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang={language}&units={unit}&appid={apiKey}"
        request = urllib.request.urlopen(url)

        # If the request returned with "OK", load the json info.
        # else print the request code.

        if request.getcode() == 200:
            data = json.loads(request.read())
            return {
                "name": data["name"],
                "temp": int(data["main"]["temp"]),
                "description": data["weather"][0]["description"],
            }
        else:
            print(f"Error: {request.getcode()}")
    except:
        return None


if __name__ == "__main__":

    # Make a request to the API.
    # Then print the info as follows,
    # "1°C, Sunny".
    # "4°C. Overcast Clouds".

    weather = makeRequest()
    if weather:
        temp = weather.get("temp")
        description = weather.get("description")
        print(f"{temp}°C, {description.title()}")
    else:
        print("Error")
