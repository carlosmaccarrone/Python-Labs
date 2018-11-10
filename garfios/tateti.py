#!/usr/bin/python
# -*- coding: utf-8 -*-
# TA-TE-TI versión beta, próximamente se pensará una interfaz 
# gráfica y conectividad P2P y cliente/servidor.
import random


def dibujarTablero(tablero):
	print '   |   |'
	print ' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3]
	print '   |   |'
	print '-----------'
	print '   |   |'
	print ' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6]
	print '   |   |'
	print '-----------'
	print '   |   |'
	print ' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9]
	print '   |   |'


def asociarLetraJugador():
	letra = ''
	while not (letra == 'X' or letra == 'O'): 
		letra = raw_input('Quiere ser X o O? ').upper()

	if letra == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']


def quienVaPrimero():
	if random.randint(0, 1) == 0:
		return 'ordenador'
	else:
		return 'jugador'


def esCasillaLibre(tablero, casilla):
# Devuelve verdadero si la casilla pasada se encuentra libre en el tablero.
	return tablero[casilla] == ' '


def movimientoJugador(tablero):
# Mientras casilla no es una casilla valida o casilla está ocupada
# sugestión: Haga su próximo movimiento
	casilla = ' '
	while casilla not in '1 2 3 4 5 6 7 8 9'.split() or not esCasillaLibre(tablero, int(casilla)):
		casilla = raw_input('Haga su próximo movimiento(1-9) ')
	return int(casilla)


def hacerUnMovimiento(tablero, letra, casilla):
	tablero[casilla] = letra


def traerTableroDuplicado(tablero):
	tablaDuplicada = []

	# Para cada elemento en elTablero copiar a tablaDuplicada
	for casilla in tablero:
		tablaDuplicada.append(casilla)

	# Devolver tablero duplicado.
	return tablaDuplicada


def movimientoAleatorioDeLista(tablero, casillas):
# Devuelve un movimiento valido pasado de la lista de casillas.
# Si no hay posibles movimientos la variable que llamó quedará NoneType.
	posiblesMovimientos = []

	for casilla in casillas:
		if esCasillaLibre(tablero, casilla):
			posiblesMovimientos.append(casilla)

	if len(posiblesMovimientos) != 0:
		return random.choice(posiblesMovimientos)


def traerMovimientoPC(tablero, letraPC):
# ALGORITMO
	if letraPC == 'X':
		letraJugador = 'O'
	else:
		letraJugador = 'X'

	# Éste bucle checa en cada iteración con elTablero que recibe la función
	# si haciendo un solo movimiento puede ganar, si es así devuelve la 
	# casilla donde debe colocar la letra para ganar.
	# Notar que en cada iteración se debe duplicar elTablero porque se
	# simula un movimiento.
	for casilla in range(1, 10):
		dup = traerTableroDuplicado(tablero)
		if esCasillaLibre(dup, casilla):
			hacerUnMovimiento(dup, letraPC, casilla)
			if esGanador(dup, letraPC):
				return casilla

	# Éste bucle checa en cada iteración con elTablero que recibe la función
	# si el jugador haciendo un solo movimiento puede ganar, si es así  
	# devuelve la casilla donde debe colocar la letra para bloquearlo.
	# Notar que en cada iteración se debe duplicar elTablero porque se
	# simula un movimiento.
	for casilla in range(1, 10):
		dup = traerTableroDuplicado(tablero)
		if esCasillaLibre(dup, casilla):
			hacerUnMovimiento(dup, letraJugador, casilla)
			if esGanador(dup, letraJugador):
				return casilla

	# Intenta colocarse en una esquina si hay alguna libre.
	casilla = movimientoAleatorioDeLista(tablero, [1, 3, 7, 9])
	if casilla != None:
		return casilla

	# Intenta colocarse en el centro si está libre.
	if esCasillaLibre(tablero, 5):
		return 5

	# Por descarte, tratará de colocarse en uno de los lados.
	return movimientoAleatorioDeLista(tablero, [2, 4, 6, 8])


def esGanador(ta, le):
# Recibe el tablero y la letra del jugador/PC, devuelve True si el jugador/PC ganó.
	return (	(ta[7] == le and ta[8] == le and ta[9] == le) or
			(ta[4] == le and ta[5] == le and ta[6] == le) or
			(ta[1] == le and ta[2] == le and ta[3] == le) or
			(ta[7] == le and ta[4] == le and ta[1] == le) or
			(ta[8] == le and ta[5] == le and ta[2] == le) or
			(ta[9] == le and ta[6] == le and ta[3] == le) or
			(ta[7] == le and ta[5] == le and ta[3] == le) or
			(ta[9] == le and ta[5] == le and ta[1] == le)	)


def seLlenoTablero(tablero):
# Devuelve True si todas las casillas del tablero tienen letra.	
	for casilla in range(1, 10):
		if esCasillaLibre(tablero, casilla):
			return False
	return True


def jugarDeNuevo():
	return raw_input('Quiere volver a intentar? (si o no) ').lower().startswith('s')


print 'TA-TE-TI by Carlitos'

while True:
	# Reset tablero
	elTablero = [' '] * 10
	letraJugador, letraPC = asociarLetraJugador()
	turno = quienVaPrimero()
	print 'El ' + turno + ' tiene el primer turno.'
	juegoEnCurso = True

	while juegoEnCurso:
		if turno == 'jugador':
		# Turno del jugador
			dibujarTablero(elTablero)
			jugada = movimientoJugador(elTablero)
			hacerUnMovimiento(elTablero, letraJugador, jugada)

			if esGanador(elTablero, letraJugador):
				dibujarTablero(elTablero)
				print 'Campeón, ganaste.'
				juegoEnCurso = False
			else:
				if seLlenoTablero(elTablero):
					dibujarTablero(elTablero)
					print 'Empate técnico'
					break
				else:
					turno = 'ordenador'

		else:
		# Turno de la PC
			jugada = traerMovimientoPC(elTablero, letraPC)
			hacerUnMovimiento(elTablero, letraPC, jugada)

			if esGanador(elTablero, letraPC):
				dibujarTablero(elTablero)
				print 'La computadora te ganó.'
				juegoEnCurso = False
			else:
				if seLlenoTablero(elTablero):
					dibujarTablero(elTablero)
					print 'Empate técnico'
					break
				else:
					turno = 'jugador'

	if not jugarDeNuevo():
		break
