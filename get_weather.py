#!/usr/bin/env python3
import argparse
import requests
import time
import json
import sys

appid = '5fb5aa8f12acef8cc32c9e1d18451077'


def get_by_city(city):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, appid)
    try:
        api_response = requests.get(url)
        api_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    data = api_response.json()
    return data


def get_by_zip(zip):
    url = "https://api.openweathermap.org/data/2.5/weather?zip={}&appid={}&units=imperial".format(zip, appid)
    try:
        api_response = requests.get(url)
        api_response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(1)
    data = api_response.json()
    return data


def parse_and_format(api_response):
    city = api_response["name"]
    temp = api_response["main"]["temp"]
    humidity = api_response["main"]["humidity"]
    temp_min = api_response["main"]["temp_min"]
    temp_max = api_response["main"]["temp_max"]
    sunrise = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(api_response["sys"]["sunrise"]))
    sunset = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(api_response["sys"]["sunset"]))
    weather = """
    The average temperature in {}  is {}{}F with a high of {}{}F and a low of {}{}F
    
    Humidity is around {}{}
    
    Sunrise will be at {} and sunset at {} 
    """.format(city, temp, '\u00b0', temp_max,'\u00b0', temp_min, '\u00b0', humidity, '\u0025', sunrise, sunset)
    return weather


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # require one of -city OR --zip but not both
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--city', action='store', nargs="+", help='the city name to fetch weather for')
    group.add_argument('-z', '--zip', action='store', help='the zip code to fetch weather for')
    args = parser.parse_args()
    if args.city:
        city = " ".join(args.city)
        response = get_by_city(city)
    else:
        response = get_by_zip(args.zip)
    weather = parse_and_format(response)
    print(weather)
