import requests
import json
from datetime import date

client_id = ""
client_secret = ""
redirect = ""

def get_ip_address():
    ip = requests.get('https://api.ipify.org').text
    return ip
  
