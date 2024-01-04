import requests
import json
from datetime import date

client_id = ""
client_secret = ""
redirect = ""

def get_ip_address():
    ip = requests.get('https://api.ipify.org').text
    return ip

def validate_ip(ip):
    if ip.lower() == 'unknown':
        return False
    ip = int(ip)
    if 0 <= ip <= 50331647:
        return False
    if 167772160 <= ip <= 184549375:
        return False
    if 2130706432 <= ip <= 2147483647:
        return False
    if 2851995648 <= ip <= 2852061183:
        return False
    if 2886729728 <= ip <= 2887778303:
        return False
    if 3221225984 <= ip <= 3221226239:
        return False
    if 3232235520 <= ip <= 3232301055:
        return False
    if ip >= 4294967040:
        return False
    return True


if 'code' not in request.args:
    params = {
        'client_id': client_id,
        'redirect_uri': redirect,
        'response_type': 'code',
        'scope': 'identify guilds',
        'state': code
    }
    return redirect('https://discordapp.com/api/oauth2/authorize' + '?' + urlencode(params))
  
