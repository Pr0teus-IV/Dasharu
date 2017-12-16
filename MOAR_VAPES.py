import requests
from bs4 import BeautifulSoup

response = requests.get("http://f1.weather.gov/MapClick.php?lat=40.71887000000007&lon=-73.97480999999996")

soup = BeautifulSoup(response.text, "html.parser")

#print(soup)

weather_curr = soup.find("p", {"class": "myforecast-current"})

weather_curr_text = weather_curr.text

print(f'The weather is currently {weather_curr_text}')
