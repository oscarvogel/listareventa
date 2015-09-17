#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cargalocalidades.py
#  
#  Copyright 2015  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from modelos import relaciones
from sistema import conectarBD


class CargaLocalidades(object):
	
	def __init__(self):
		self.__relaciones__ = relaciones.Relaciones()
	
	def InsertaLocalidades(self, ventana = None):
		self.__relaciones__.tipo = 'mysql'
		query = """select codigo, nombre, distancia, provincia,
				codpos, fletep1, fletetn1,
				fletep4, fletetn4,
				boni1, boni4, zona, reparto, 
				IntTnL1, IntTnL4, 
				IntPorL1, IntPorL4 
			from localidad"""
		localidades = self.__relaciones__.ConsultaTodo(query)
		self.__relaciones__.tipo = None
		
		total = float(len(localidades))
		reg = 1.0
		query = "delete from localidad"
		self.__relaciones__.EjecutaSQL(query)
		for data in localidades:
			if ventana is None:
				print data
			else:
				ventana.StatusBar.SetStatusText("Trayendo datos de " + data[1])
				ventana.avance.SetValue(reg / total * 100)
				reg += 1
				
			query = """insert into localidad (codigo, nombre, distancia, provincia, codpos, fletep1, fletetn1,
				fletep4, fletetn4, boni1, boni4, zona, reparto, inttnl1, inttnl4, intporl1, intporl4)
				values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
			"""
			#parametros.append(data)
			parametros = [data[0], data[1], int(data[2]), data[3], data[4],
						float(data[5]), float(data[6]), float(data[7]), float(data[8]), float(data[9]),
						float(data[10]), data[11], data[12], float(data[13]), float(data[14]),
						float(data[15]), float(data[16])]
			self.__relaciones__.EjecutaSQL(query, parametros)
			
if __name__ == "__main__":
	c = CargaLocalidades()
	c.InsertaLocalidades()
