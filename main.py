import requests
import json
from datetime import date

client_id = ""  #id da secret
client_secret = "" #secret
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

if 'code' in request.args:
    token_request = "https://discordapp.com/api/oauth2/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect,
        "state": request.args.get('state'),
        "code": request.args.get('code')
    }
    token_response = requests.post(token_request, data=token_data)
    token_data = json.loads(token_response.text)
    access_token = token_data['access_token']

info_request = "https://discordapp.com/api/users/@me"
info_headers = {
    "Authorization": "Bearer " + access_token
}
info_response = requests.get(info_request, headers=info_headers)
user = json.loads(info_response.text)
id = user['id']
un = user['username']
di = user['discriminator']
diname = un + "#" + di
ip = get_ip_address()

if id:
    ip_info_response = requests.get("http://extreme-ip-lookup.com/json/" + ip)
    ip_info = json.loads(ip_info_response.text)
    country = ip_info['country']
    today = date.today().strftime("%d/%m/%Y")
    with open("logs.txt", "a+") as file:
        file.write("Logged IP: " + ip + " (" + diname + ") - (" + id + ") - (" + country + "), at " + today + "\n")

print("<title>Hi</title>")
