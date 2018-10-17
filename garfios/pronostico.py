## -*- coding: utf-8 -*-
#Pronostico del tiempo en San Andrés, Buenos Aires
#Carlos Esteban Maccarrone -cem- 2018
 
import requests, json

r = requests.get('https://ws.smn.gob.ar/map_items/weather')
if(r.status_code == 200):
	datos = json.loads(r.text)
	print datos[35]['weather']['tempDesc']
