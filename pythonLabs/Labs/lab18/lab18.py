import json
from urllib.request import urlopen
from urllib.error import HTTPError


def location_lookup():
    try:
        return json.load(urlopen('http://ipinfo.io/json'))
    except HTTPError:
        return False


def get_current_location():
    location = location_lookup()
    latlon: str = location['loc']
    latlon_array = latlon.split(sep=",")
    return latlon_array


coordinates = get_current_location()
keywords = ['restaurant']
radius = '1000'
api_key = ''

import pandas as pd, numpy as np
import requests
import json
import time
from google.colab import files

for coordinate in coordinates:
    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinate+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
        while True:
            print(url)
            respon = requests.get(url)
            jj = json.loads(respon.text)
            results = jj['results']
            for result in results:
                name = result['name']
                place_id = result ['place_id']
                lat = result['geometry']['location']['lat']
                lng = result['geometry']['location']['lng']
                rating = result['rating']
                types = result['types']
                vicinity = result['vicinity']
                data = [name, place_id, lat, lng, rating, types, vicinity]
                final_data.append(data)
                time.sleep(5)
                if 'next_page_token' not in jj:
                    break
                else:
                    next_page_token = jj['next_page_token']
                    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key='+str(api_key)+'&pagetoken='+str(next_page_token)
labels = ['Place Name','Place ID', 'Latitude', 'Longitude', 'Types', 'Vicinity']