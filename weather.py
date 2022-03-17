# Import libraries
import imp
from urllib import request
from requests_html import HTMLSession
from trycourier import Courier
import os

client = Courier(auth_token="token")

# Set the URL you want to webscrape from
s = HTMLSession()

url = 'https://www.google.com/search?client=opera-gx&q=wetter+wörthsee&sourceid=opera&ie=UTF-8&oe=UTF-8'
# Connect to the URL
response = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.70'})

temp = response.html.find('span#wob_tm', first = True).text
clouds = response.html.find('div.VQF4g', first=True).find('span#wob_dc', first = True).text
count = 0 

names = ['user']
mailadress = [user@domain.com]

for i in names:
  resp = client.send_message(
    message={
      "to": {
        "email": mailadress[count],
      },
      "template": "3WB3F9RJ7ZMX2EQK6DXR0WVXQWN8",
      "data": {
        "recipientName": i,
        "place": "Wörthsee",
        "cond": clouds,
        "temp": temp + "°C",
      },
    }
  )
  count += 1

print(temp + ' °C')
print(clouds)

