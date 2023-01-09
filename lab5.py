# -*- coding: utf-8 -*-
"""lab5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mxnfEuX9HbTnKC-gj6U8d3Z8V6b0Q4-U
"""

import requests
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Tester")
city_name = str(input('Введите адрес: \n'))
location = geolocator.geocode(city_name)

print(location)
print(location.latitude, location.longitude)

url1 = ('http://api.openweathermap.org/data/2.5/weather?'
         'lat='+str(location.latitude)+'&'
         'lon='+str(location.longitude)+'&'
         'appid=7cdcfaa69a322e2c77fdf3043de45290&'
         'units=metric&'
         'lang=ru')

r1 = requests.get(url1)
r1 = r1.json()
print("погода в " + city_name + ":", r1['weather'][0]['description'])
print("температура:", r1['main']['temp'], "по Цельсию")
print("давление:", r1['main']['pressure'], "гекто-паскаль")
print("влажность:", r1['main']['humidity'], "%")
with open('requests1.json', 'w') as file_1:
    json.dump(r1, file_1, indent=3)

url2 = ('https://newsapi.org/v2/everything?'
         'q=bbc-news&'
         'from=2023-01-09&'
         'sortBy=popularity&'
         'apiKey=694c15265e8c435fbc7d9e827ca5e917'
         )

r2 = requests.get(url2)
r2 = r2.json()
with open('requests2.json', 'w') as file_2:
    json.dump(r2, file_2, indent=3)

url3 = ('https://api.nasa.gov/planetary/earth/imagery?'
        'lon='+str(location.longitude)+'&'
        'lat='+str(location.latitude)+'&'
        'date=2023-01-09&'
        'api_key=aI7Gf93e7nBH4622wR2Njx4nMbBjVBCCi5exJQJJ')

r3 = requests.get(url3)
r3 = r3.json()
with open('requests3.json', 'w') as file_3:
    json.dump(r3, file_3, indent=3)
