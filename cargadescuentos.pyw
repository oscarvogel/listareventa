#!/usr/bin/python
# -*- coding: utf-8 -*-

from modelos import relaciones
from sistema import conectarBD


class CargaDescuentos(object):
	
	def __init__(self):
		self.__relaciones__ = relaciones.Relaciones()
	
	def InsertaDescuentos(self, ventana = None):
		self.__relaciones__.tipo = 'mysql'
		query = """
			select id, cliente, desdeart, hastaart, descuento
				from descuento
		"""
		descuentos = self.__relaciones__.ConsultaTodo(query)
		self.__relaciones__.tipo = None
		
		total = float(len(descuentos))
		reg = 1.0
		query = "delete from descuento"
		self.__relaciones__.EjecutaSQL(query)
		
		for data in descuentos:
			if ventana is None:
				print data
			else:
				ventana.StatusBar.SetStatusText("Trayendo datos de " + data[1])
				ventana.avance.SetValue(reg / total * 100)
				reg += 1
				
				
			query = """insert into descuento (id, cliente, desdeart, hastaart, descuento)
				values(?, ?, ?, ?, ?)
			"""
			#parametros.append(data)
			parametros = [data[0], data[1], data[2], data[3], float(data[4])]
			self.__relaciones__.EjecutaSQL(query, parametros)
			
if __name__ == "__main__":
	c = CargaDescuentos()
	c.InsertaDescuentos()
