# -*- coding:utf-8 -*-

import requests
import urllib3
import time
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_page(lat, lng):
    user_agent = 'Mozilla/5.0 (Linux; Android 7.0; EVA-AL10 Build/HUAWEIEVA-AL10; wv)' \
                 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044030 ' \
                 'Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) ' \
                 'NetType/WIFI Language/zh_CN MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN'

    headers = {'User-Agent': user_agent,
               'Content-Type': 'application/x-www-form-urlencoded',
               'charset': 'utf-8',
               'host': 'cwx.mobike.com',
               }

    data = {'errMsg': 'getLocation=ok',
            'longitude': lng,
            'latitude': lat,
            }

    url = 'https://mwx.mobike.com/nearby/nearbyBikeInfo'
    req = requests.post(url=url, data=data, headers=headers, verify=False)
    return req.json()['object']


def find_bike(diction, bikes):
    for data in bikes:
        bike = {}
        bike['type'] = data['type']
        bike['time'] = now_time
        bike['distX'] = data['distX']
        bike['distY'] = data['distY']
        bike_dict[data['bikeIds'].encode()] = bike


def write_csv(bike_dict, tms):
    with open('mobike_loc-%s.csv' % tms, 'wb') as f:
        writers = csv.writer(f)
        writers.writerow(['bikeid', 'biketype', 'time', 'longitude', 'latitude'])
        for row in bike_dict:
            writers.writerow([row,
                              bike_dict[row]['type'],
                              bike_dict[row]['time'],
                              bike_dict[row]['distX'],
                              bike_dict[row]['distY']])


def get_map():
    gaode_url = 'http://restapi.amap.com/v3/staticmap'
    data = {'key': '9b3b38d0b8f619ddf38941ad997ac81f',
            'location': '120.262277,31.488689',
            'zoom': '13',
            'size': '750*750',
            'markers': 'mid,,'
            }
    gaode_url = 'http://restapi.amap.com/v3/staticmap?key=%s&location=%s&zoom=%s&size=%s' % (data['key'], data['location'], data['zoom'], data['size'])
    req = requests.post(url=gaode_url, data=data)
    return req


location = [('120.262277', '31.488689'), ('120.268457', '31.488689'), ('120.272491', '31.488689'),
            ('120.262277', '31.484225'), ('120.268457', '31.484225'), ('120.272491', '31.484225'),
            ('120.262277', '31.478845'), ('120.268457', '31.478845'), ('120.272491', '31.478845')]

if __name__ == '__main__':
    while 1:
        bike_dict = {}
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        write_time = time.strftime("%Y%m%d-%H%M%S", time.localtime())[-11:-2]
        for i in location:
            bikes = get_page(i[1], i[0])
            find_bike(bike_dict, bikes)
        # print bike_dict
        write_csv(bike_dict, write_time)
        print write_time, 'csv writing!!! '
        time.sleep(180)
