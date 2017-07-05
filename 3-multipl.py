#!/usr/bin/python

#<?php
#        $contador = 0;
#
#        while ($contador <= 100)
#        {
#                $resto1 = $contador % 3;
#                $resto2 = $contador % 5;
#
#                if ($resto1 == 0)
#                        printf("%d es divisible por 3<br>",$contador);
#
#                if ($resto2 == 0)  //idem bloque superior
#                        printf("%d es divisible por 5<br>",$contador);
#
#                $contador++;
#        }
#?>

import sys


#chequea que la cantidad de argumentos se la correcta
if len(sys.argv) != 2:
        print "Uso: " + sys.argv[0] + " numero"
        sys.exit(1)


#Asigna la variable cont en 0
cont = 0

#Ejecuta while mientras que cont sea menor que el argumento pasado
while cont <= int(sys.argv[1]):

	#calcula el resto de la division de cont por 3 y 5
	resto1 = cont % 3
	resto2 = cont % 5

	#si el resto es 0 es porque el numero es multiplo
	if resto1 == 0:
		print str(cont) + " es multiplo de 3"
	if resto2 == 0:
		print str(cont) + " es multiplo de 5"
	#suma contador (es lo mismo que cont=cont + 1) es C y PHP se puede poner tambien asi: cont++
	cont+=1
