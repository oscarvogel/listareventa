#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from modelos import relaciones
from sistema import conectarBD


class Pagos(object):
	
	def TraeDatos(self, cLista):
		rel = relaciones.Relaciones()
		
		codigos = rel.ConsultaTodo( consulta = "select * from pagos where lista = '" + cLista + "' or lista = ''")
		valores = []
		for codigo in codigos:
			valores.append(codigo[0] + '-' + codigo[1])
		
		return valores
		
	def __repr__(self):
		return "<Pagos(pago='%s', detalle='%s'')>" % (
			self.pago, self.detalle)
