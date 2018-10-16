#!/usr/bin/python
## -*- coding: latin-1 -*-

import threading, httplib2
from bs4 import BeautifulSoup

http = httplib2.Http()
cabecera = {'User-Agent': 'Mozilla/5.0'}

url = raw_input('Googlear: ')
print '\n'
url = url.replace(' ','+')
url = 'https://www.google.com/search?q=' + url

respuesta = http.request(url, headers=cabecera )

def busqueda(contador, semaforo):
	indice = contador - 1

	if(contador == 0):
		print respuesta[0].status
		for web in BeautifulSoup(respuesta[1], 'lxml').find_all('h3', class_='r'):
			try:
				if( '/search?q=' in web.find('a')['href']):
					print "Pagina 1"
					print web.find('a')['href'].replace('/search?q=', 'https://www.google.com/search?q=') +'\n'
				else:
					print "Pagina 1"
					print web.find('a')['href'].replace('/url?q=', '') +'\n'
			except AttributeError, KeyError:
				pass

	if(contador == 1):
		for web in BeautifulSoup(respuesta[1], 'lxml').find_all('div', {'id' : 'foot'}):
			try:
				paginaDos = http.request( 'https://www.google.com' + web.find_all('a', class_='fl')[indice]['href'], headers=cabecera )
				print paginaDos[0].status
				for web in BeautifulSoup(paginaDos[1], 'lxml').find_all('h3', class_='r'):
					try:
						print "Pagina 2"
						print web.find('a')['href'].replace('/url?q=', '') +'\n'
					except AttributeError, KeyError:
						pass
			except AttributeError, KeyError:
				pass

	if(contador == 2):
		for web in BeautifulSoup(respuesta[1], 'lxml').find_all('div', {'id' : 'foot'}):
			try:
				paginaTres = http.request( 'https://www.google.com' + web.find_all('a', class_='fl')[indice]['href'], headers=cabecera )
				print paginaTres[0].status
				for web in BeautifulSoup(paginaTres[1], 'lxml').find_all('h3', class_='r'):
					try:
						print "Pagina 3"
						print web.find('a')['href'].replace('/url?q=', '') +'\n'
					except AttributeError, KeyError:
						pass
			except AttributeError, KeyError:
				pass

	semaforo.release()

threads = list()
sem = threading.BoundedSemaphore(value=1)
for i in range(3):
	t = threading.Thread(target=busqueda, args=(i, sem))
	threads.append(t)
	sem.acquire()
	t.start()



# Éste programa buscará en google, y mostrará
# las primeras tres páginas de resultados

# Para acceder a los links desde él terminal
# mantenga pulsado Ctrl y haga click sobre el link

# pip install httplib2 beautifulsoup4
