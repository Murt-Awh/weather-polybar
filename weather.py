import json
import urllib.request

apiKey="XXXXXXXX"
city="manchester"
language="en"
unit="metric"

def makeRequest():
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q=${city}&lang=${language}&units=${unit}&appid={apiKey}"
        request = urllib.request.urlopen(url)
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
    weather = makeRequest()
    if weather:
        name = weather.get("name")
        temp = weather.get("temp")
        description = weather.get("description")
        print(f"{temp}°C, {description.title()}")
    else:
        print("Error")
