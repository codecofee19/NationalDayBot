#!/usr/local/bin/python
import requests
from bs4 import BeautifulSoup
import re
from twilio.rest import Client
days = requests.get("http://www.nationaldaycalendar.com/latest-posts/")
result = BeautifulSoup(days.content, 'html.parser')

heres = result.find('h2')

ACCOUNT_SID = "AC759deff6bd5c457a6c3defab745e8a52"

AUTH_TOKEN = "8b5ce56dd56c9f2d5f016a700bc78a4a"

client = Client(ACCOUNT_SID, AUTH_TOKEN)
client.messages.create(
  to="+19037470216",
  from_="+19034833269",
  body=heres.get_text(),
  media_url="https://climacons.herokuapp.com/clear.png",
)



