#!/usr/bin/python
## -*- coding: utf-8 -*-

import logging, datetime, sys, os

rutaRegistro = os.getcwd()
fechaAhora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

try:

	def unaFuncion():

		print "Hola mundo\n como estas?"
		
		raise Exception('Esto es una excepcion controlada')
		
		"""
		Aquí va el código de la función
		+++							++++
			***					***
				+++			+++
					******
		Aquí va el código de la función
		"""	


	unaFuncion()


except Exception as e:
	tipoExcepcion, valorExcepcion, rastroExcepcion = sys.exc_info()
	fname = os.path.split(rastroExcepcion.tb_frame.f_code.co_filename)[1]
	print "\n"+str(e)+" in "+str(fname)+" - linea "+str(rastroExcepcion.tb_lineno)+"\n"

	logging.basicConfig(filename="registroErrores.txt", level=logging.INFO)
	registro = open (rutaRegistro+"/registroErrores.txt", "a")
	registro.write(fechaAhora+"\n\n"+\
		str(e)+" in "+str(fname)+" - linea "+str(rastroExcepcion.tb_lineno)\
		+"\n-------------------------------------------------------------------------------\n")
	registro.close()
