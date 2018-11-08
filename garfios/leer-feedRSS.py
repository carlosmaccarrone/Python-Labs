#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.clarin.com/rss.html

import urllib
from xml.dom import minidom

def traerURLdeNodos(nodo):
	return ''.join([n.nodeValue for n in nodo.childNodes if n.nodeType == n.TEXT_NODE])
									# Cambiar por el feed que guste
doc = minidom.parse(urllib.urlopen('https://www.clarin.com/rss/politica/'))

print '<h1>Python news</h1>'
print '<o1>'
for item in doc.getElementsByTagName('item')[:3]:
	print '<li>\n <a href="%s">%s</a>\n </li>' % (traerURLdeNodos(item.getElementsByTagName('link')[0]), traerURLdeNodos(item.getElementsByTagName('title')[0]))
	print '</o1>'
