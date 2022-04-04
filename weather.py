import requests


def current_weather(city:str):
    with open("api.txt", "r") as file:
        API_Key = file.read()

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


    request_url = f"{BASE_URL}?appid={API_Key}&q={city}"

    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = round(data["main"]["temp"]-273.15, 2)
        location = data["name"]

        if temperature > 10:
            DressWarm = "No need to dress warmly"
        else:
            DressWarm = "Consider dressing warmly"

        return f"Good Morning! The current weather in {location} is '{weather}' and the current temperature is: {temperature} celsius. {DressWarm}!"
    else:
        return "An error has occurred"


