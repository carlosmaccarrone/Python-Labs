#!/usr/bin/python

#<?php
#        echo "<b>Otra version</b><br>";
#
#        for ($i=0; $i<=100; $i++)
#                if ( !($i % 3) && !($i % 5) )
#                        printf("%d es multiplo de 3 y 5<br>", $i);
#
#?>

import sys

#chequea qeu la cantidad de argumentos sea la correcta, si no imprime uso y sale con error
if len(sys.argv) != 2:
        print "Uso: " + sys.argv[0] + " numero"
        sys.exit(1)

for i in range(int(sys.argv[1])):
	if not (i % 3) and not (i % 5):    # aca se chequea que el valor de (i % 3) negado sea verdadero, python considera 0 como falso y algun valor como verdadero
		print str(i) + " es multiplo de 3 y 5"
