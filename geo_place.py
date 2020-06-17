# python version 3.7.0

import requests
import json


MAPQUEST_API_KEY = '290X23ygvkVlFPAyFjIUiDUTLikmaRpn' # Ключ от API


def extract_lat_long_via_address(address):
   lat =  None # Широта
   lng = None # Долгота
   api_key = MAPQUEST_API_KEY
   # Строим ссылку
   base_url = "http://www.mapquestapi.com/geocoding/v1/address"
   endpoint = f"{base_url}?key={api_key}&location={address}"
   
   
   # Делаем запрос по нашей ссылке
   r = requests.get(endpoint)
   #print(r.status_code)
   # Извлекаем нужные данные из формата json
   results = r.json()['results'][0]
   #print(results)
   lat = results['locations'][0]['displayLatLng']['lat']
   lng = results['locations'][0]['displayLatLng']['lng']
   return lat, lng




