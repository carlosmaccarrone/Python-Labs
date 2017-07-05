#!/usr/bin/python

#importa libreria sys
import sys


#chequea que la cantidad de argumentos en el comando sea correcta y si no sale con error
#chequea que que la cantidad de argumentos no sea menor que 3, esto es "./mayor.py numero1 numero2" tiene que tener 3 palabras. Para contar el numero de palabras se usa la funcion len()

if len(sys.argv) != 3:

	#si hay menos de 3 argumentos se imprime el modo de uso y se sale con error sys.exit() con codigo 1
	print "Uso: " + sys.argv[0] + " numero1 numero2"
	sys.exit(1)

#asigna los argumentos pasados por comando a variables y los transforma de strings a enteros
a = int(sys.argv[1])
b = int(sys.argv[2])

#Comaraciones para ver cual es mayor
if a > b:
	print str(a) + " es mayor que " + str(b)
if b > a:
	print str(b) + " es mayor que " + str(a)
if a == b:
	print str(b) + " y " + str(a) + " son iguales"
