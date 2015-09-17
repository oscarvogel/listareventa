#!#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Retorna un objeto conexion, o None si no se pudo conectar a la base de datos.
El programa que use este modulo se debe encargar de liberar la conexion.
Forma parte del paquete sistema.
Modificado 18/10/2011 - SQLite
"""
import MySQLdb, sqlite3, os
import leerProp
# --------------------------------------------------------------------

class ConectarBD(object):

	def __init__(self, tipo = None):
		# Atributo oculto que indica la conexion
		self.__db = None
		
		# Lee el archivo de propiedades para extraer la informacion de la Base de Datos.
		# Estos datos vienen en un diccionario.
		config = leerProp.armarDicc( os.path.join('sistema', 'app.config') )
		
		if tipo is None:
			self.__db = sqlite3.connect( os.path.abspath( config['bdPATH'] ) )
		elif tipo.upper() == 'MYSQL':
			# En el archivo /etc/mysql/my.cnf esta el verdadero nombre del servidor, puede ser la IP o nombre
			
			self.__db = MySQLdb.connect(host  = config['bdHOST'],
									user   = config['bdUSER'],
									passwd = 'fasca',
									db     = 'fasa',
									charset = 'utf8')
			#self.__engine = create_engine('mysql+mysqldb://' + config['bdUSER'] + ':fasca@' + config['bdHOST'] + '/fasa')
		else:
			self.__db = sqlite3.connect(config['bdPATH'])
			
	# Metodo de acceso al atributo conexion
	def get_bd(self):
		return self.__db

# --------------------------------------------------------------------

# Esto solamente se usa para probar el modulo
if __name__ == '__main__':
	a = ConectarBD()
	if (a.get_bd() == None):
		print 'Sin conexion'
	else:
		print 'OK'
