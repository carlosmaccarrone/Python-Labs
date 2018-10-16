#!/usr/bin/python
## -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/verArchivo/<path:infile>")
def traerArchivo(infile):
	with open(infile, "r") as archivo:
		texto = archivo.read()
		return texto

if __name__ == '__main__' :
	app.run(host='192.168.1.6', port=3267)



# Éste programa visualiza en un website
# un archivo cualquiera (txt, csv, etc),
# creando un servidor flask en
# 192.168.1.6:3267/verArchivo/<nombre del archivo>
# el archivo que se desea ver debe estar
# copiado en la ruta desde donde se ejecuta
# éste programa.