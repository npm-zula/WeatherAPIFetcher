import requests


API_KEY = "7afeef7a972b2b16ad20d84ee78791cf"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city  = input("Enter the favorite City name: ")


request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if(response.status_code == 200):
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"Weather is: {weather}")
    temp = data['main']['temp'] - 273
    print(f"Temperature: {round(temp,2)} Celsius")

else:
    print("ERROR ERROR")

