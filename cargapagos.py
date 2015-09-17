#!/usr/bin/python
# -*- coding: utf-8 -*-

from modelos import relaciones
from sistema import conectarBD


class CargaPagos(object):
	
	def __init__(self):
		self.__relaciones__ = relaciones.Relaciones()
	
	def InsertaPagos(self, ventana = None):
		self.__relaciones__.tipo = 'mysql'
		query = """
			select pago, detalle, lista, punitorio, des1, dia, tipo
				from pagos
		"""
		pagos = self.__relaciones__.ConsultaTodo(query)
		self.__relaciones__.tipo = None
		
		total = float(len(pagos))
		reg = 1.0
		query = "delete from PAGOS"
		self.__relaciones__.EjecutaSQL(query)
		for data in pagos:
			if ventana is None:
				print data
			else:
				ventana.StatusBar.SetStatusText("Trayendo datos de " + data[1])
				ventana.avance.SetValue(reg / total * 100)
				reg += 1
				
				
			query = """insert into pagos (pago, detalle, lista, punitorio, des1, dia, tipo)
				values(?, ?, ?, ?, ?, ?, ?)
			"""
			#parametros.append(data)
			parametros = [data[0], data[1], data[2], float(data[3]), float(data[4]), data[5], data[6]]
			self.__relaciones__.EjecutaSQL(query, parametros)
			
if __name__ == "__main__":
	c = CargaPagos()
	c.InsertaPagos()
