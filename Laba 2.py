import requests as requests

API_KEY = "62f9462b75496d0e801176e538dd82f9"

city_name = "Kelsey"
country_code = "CA"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}"
response = requests.get(url)
data = response.json()
wind_speed = data["wind"] ["speed"]
visibility = data["visibility"]
print(f"Wind Speed:  {wind_speed} m/s")
print (f"Visibility:  {visibility} meters")