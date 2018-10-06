## -*- coding: latin-1 -*-
import json, io, sys
reload(sys)
sys.setdefaultencoding('latin-1')

nombre_ = ['Carlos', 'Diego', 'Alberto']

telefono_ = ['4755-6582', '1523768', '127001']

direccion_ = ['Islas Malvinas', 'Los Áromos 456', 'El Arroyíto 0123']

archivo = json.dumps( [ {'Nombre' : x, 'Teléfono' : y, 'Dirección' : z } 
						for x, y, z in zip(nombre_, telefono_, direccion_ ) ]
						, ensure_ascii=False, indent=3, separators=(',', ': '))

with io.open('datos.json', 'w', encoding='latin-1') as json_file:
	datos = unicode( archivo )
	json_file.write( datos )
