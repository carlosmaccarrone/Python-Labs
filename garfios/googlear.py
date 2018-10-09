#!/usr/bin/python
## -*- coding: latin-1 -*-
import sys
reload(sys)
sys.setdefaultencoding('latin-1')
 
import httplib2
from bs4 import BeautifulSoup

http = httplib2.Http()
cabecera = {'User-Agent': 'Mozilla/5.0'}

url = raw_input('Googlear: ')
print '\n'
url = url.replace(' ','+')
url = 'https://www.google.com/search?q=' + url

respuesta = http.request(url, headers=cabecera)

for web in BeautifulSoup(respuesta[1], 'lxml').find_all('h3', class_='r'):
	try:
		print web.find('a')['href'].replace('/url?q=', '') +'\n'
	except AttributeError, KeyError:
		pass


# Éste programa buscará en google, y mostrará
# los websites de los primeros diez resultados

# Para acceder a los links desde él terminal
# mantenga pulsado Ctrl y haga click sobre el link 

# pip install httplib2 beautifulsoup4
