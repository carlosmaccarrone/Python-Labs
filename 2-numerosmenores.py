#!/usr/bin/python

import sys

#chequea que la cantidad de argumentos sea la correcta, si no imprime el modo de uso y sale con error
if len(sys.argv) != 2:
	print "Uso: " + sys.argv[0] + " numero"
	sys.exit(1)


#inicia la variable i en 0
i=0

#bucle while, mientras que i sea menor o igual que el numero pasado como argumento se ejecuta el codigo del while
#imprime el numero y le suma 1 (i+=1 es lo mismo que poner i = i + 1)

while i <= int(sys.argv[1]):
	print i
	i+=1
