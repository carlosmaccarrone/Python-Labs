import requests as req
import json

url = 'https://www.google.com/'

response = req.get(url)

headers = response.headers

#print headers

datos = json.dumps( dict(headers), ensure_ascii=False, indent=3, separators=(',', ': ') )

#print datos

with open('HTTPHeaders.json', 'w') as json_file:
	json_file.write( datos )