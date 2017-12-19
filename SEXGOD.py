import requests

from bs4 import BeautifulSoup

import time

prev_temp_int = 0

while True:

    response = requests.get("https://weather.com/weather/today/l/11237:4:US")

    soup = BeautifulSoup(response.text, "html.parser")

    temp_el = soup.find("span", {"class": "styles-xz0ANuUJ__temperature__3Ph8k"})

    temp_str = temp_el.text.strip('°')

    temp_int = int(temp_str)

    if temp_int != prev_temp_int:
        print(f'TEMP NOW EQUALS {temp_int}°')

    prev_temp_int = temp_int

    time.sleep(5)

