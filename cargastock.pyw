#!/usr/bin/python
# -*- coding: utf-8 -*-

from modelos import relaciones
from sistema import conectarBD
from sistema import funciones

class CargaStock(object):
	
	def __init__(self):
		self.__relaciones__ = relaciones.Relaciones()
		self.__funciones__ = funciones.Funciones()
		
		
	def ActualizaStock(self, ventana = None):
		
		info = self.__relaciones__.ConsultaUno("select * from info")
		
		self.__relaciones__.tipo = 'mysql'
		self.__relaciones__.diccionario = True
		parametros = str(info[1])
		
		if parametros == '':
			query = "select * from lista order by codigo"
		else:
			query = "Select * From lista where ultact >= " + parametros + " Order By codigo"
		
		stock = self.__relaciones__.ConsultaTodo(query)
		self.__relaciones__.tipo = None
		self.__relaciones__.diccionario = False
		total = float(len(stock))
		reg = 1.0
		
		if total == 0:
			self.__funciones__.Info("No hay actualizaciones de precios disponibles", ventana)
			
		for d in stock:
			if not ventana is None:
				ventana.avance.SetValue(reg / total * 100)
				reg += 1
				ventana.StatusBar.SetStatusText("Trayendo datos de " + d['detalle'])
			else:
				print d
				
			if self.__relaciones__.EncuentraClave('lista','codigo', d['codigo']):
				query = """
					update lista
						set unidad = ?, detalle = ?, peso = ?, espesor = ?, iva = ?,
							mts2 = ?, precio1 = ?, precio4 = ?, reparto = ?,
							redferre = ?, tiporeparto = ?, campoa1 = ?, preciopub = ?,
							recargo = ?, reducida = ?, pbl1ret = ?, pbl4ret = ?,
							pbl1rep = ?, pbl4rep = ?, estado = ?
						where codigo = ?
				"""
				parametros = d['unidad'], d['detalle'], d['peso'], d['espesor'], d['iva'],\
					d['mts2'], d['precio1'], d['precio4'], d['reparto'], d['redferre'], \
					d['tiporeparto'], d['campoa1'], d['preciopub'], d['recargo'], d['reducida'], \
					d['pbl1ret'], d['pbl4ret'], d['pbl1rep'], d['pbl4rep'], ' ', d['codigo']
				self.__relaciones__.EjecutaSQL(query, parametros)
			else:
				query = """
					insert into lista
						(codigo, unidad, detalle, peso, espesor, iva,
							mts2, precio1, precio4, reparto, redferre, tiporeparto,
							campoa1, reducida, preciopub, recargo, estado, pbl1ret,
							pbl4ret, pbl1rep, pbl4rep )
						values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
				"""
				parametros =  d['codigo'], d['unidad'], d['detalle'], d['peso'], d['espesor'], d['iva'],\
					d['mts2'], d['precio1'], d['precio4'], d['reparto'], d['redferre'], \
					d['tiporeparto'], d['campoa1'], '', d['preciopub'], d['recargo'], d['reducida'], \
					d['pbl1ret'], d['pbl4ret'], d['pbl1rep'], d['pbl4rep']
				self.__relaciones__.EjecutaSQL(query, parametros)
				
				
if __name__ == "__main__":
	c = CargaStock()
	c.ActualizaStock()
