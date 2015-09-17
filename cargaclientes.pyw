#!/usr/bin/python
# -*- coding: utf-8 -*-

from modelos import relaciones
from sistema import conectarBD


class CargaClientes(object):
	
	def __init__(self):
		self.__relaciones__ = relaciones.Relaciones()
	
	def InsertaClientes(self, ventana = None):
		info = self.__relaciones__.ConsultaUno("select * from info")
		
		self.__relaciones__.tipo = 'mysql'
		self.__relaciones__.diccionario = True
		parametros = str(info[1])
		
		if parametros == '':
			query = "select * from clientes order by codigo"
		else:
			query = "Select * From clientes where ultact >= " + parametros + " Order By codigo"
		
		cli = self.__relaciones__.ConsultaTodo(query)
		self.__relaciones__.tipo = None
		total = float(len(cli))
		reg = 1.0
		
		for d in cli:
			if not ventana is None:
				ventana.avance.SetValue(reg / total * 100)
				reg += 1
				ventana.StatusBar.SetStatusText("Trayendo datos de " + d['dato'])
			else:
				print d
			
			if self.__relaciones__.EncuentraClave('clientes','codigo', d['codigo']):
				query = """
					update clientes
						set lista = ?, nombre = ?, localidad = ?, pago = ?
						where codigo = ?
				"""
				parametros = d['lista'], d['dato'], d['loc_cod'], d['pago'], d['codigo']
			else:
				query = """
					insert into clientes
						(codigo, lista, nombre, localidad, pago)
						values( ?, ?, ?, ?, ?)
				"""
				parametros = d['codigo'], d['lista'], d['dato'], d['loc_cod'], d['pago']
			self.__relaciones__.EjecutaSQL(query, parametros)
			
			
if __name__ == "__main__":
	c = CargaClientes()
	c.InsertaClientes()
