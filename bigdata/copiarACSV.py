## -*- coding: utf-8 -*-
# Carlos Estebab Maccarrone -cem- 2018
import argparse
import apache_beam as beam
from apache_beam.io import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from beam_utils.sources import CsvFileSource
from apache_beam.io.filesystem import CompressionTypes as ct
import sys
reload(sys)
sys.setdefaultencoding('latin-1')

def traerColumnas(argv=None):

	parser = argparse.ArgumentParser()

	parser.add_argument('-in',
	                  dest='input',
	                  required=True,
	                  help='Archivo de entrada')

	parser.add_argument('-out',
	                  dest='output',
	                  required=True,
	                  help='Archivo de salida')

	known_args, pipeline_args = parser.parse_known_args(argv)

	pipeline_options = PipelineOptions(pipeline_args)
	
	p = beam.Pipeline(options=pipeline_options)

	DATOS = (
	    p
	    | 'read_files' >> beam.io.Read(
	        CsvFileSource(known_args.input,
	                      compression_type = ct.UNCOMPRESSED))

	    # Se descartan las filas que no tienen las columnas indicadas
	    | 'filter_rows' >> beam.Filter(lambda x: ('Nombre de la Unidad Económica' in x and
	                                              'Número de teléfono' in x))

	    # Se guardan las columnas que le son indicadas
	    | 'filter_columns' >> beam.Map(
	        lambda x: ','.join( tuple(( x['Nombre de la Unidad Económica'].strip() ,
	                           x['Número de teléfono'].strip()  ) )).encode('latin-1')       ))
	
	DATOS | 'write' >> beam.io.WriteToText(known_args.output, file_name_suffix='.csv', shard_name_template='', header='Nombre de la Unidad Económica, Número de teléfono')

	result = p.run()

traerColumnas()

#Propósito
#Éste programa crea un archivo .csv a partir de otro archivo con las columnas
#que le sean solicitadas del archivo de origen.

#Modo de uso

#Se llama al programa python pasandole los argumentos, un origen 
#(archivo .csv) y un destino donde depositar los resultados.
# $ python copiarACSV.py -in siete.csv -out salida/ejemplo

#El programa creara el archivo de salida ejemplo.csv en la 
#carpeta salida, con las columnas que usted selecione del 
#archivo de origen.
#Si llegara a presentar éste problema 
# " ImportError: cannot import name fileio " 
#visite https://stackoverflow.com/questions/46787428/python-from-apache-beam-io-import-fileio-gives-error-cannot-import-name-filei 
#para su posterior solución.
