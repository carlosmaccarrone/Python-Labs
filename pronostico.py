## -*- coding: utf-8 -*-
#Pronostico del tiempo en San Andrés, Buenos Aires
#Carlos Esteban Maccarrone -cem- 2018
 
import requests
import json

r = requests.get('https://ws.smn.gob.ar/map_items/weather')
r.status_code

datos = json.loads(r.text)

print datos[35]['weather']['tempDesc']
