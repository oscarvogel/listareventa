#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	from modelos import relaciones
	from sistema import globalDef

except:
	import sys
	sys.path.append('x:\\fasapython\\listareventa\\')
	from modelos import relaciones
	from sistema import globalDef


class Calcula(object):
	
	#inicializacion de variables
	Descuento = 0.00 #descuento por la condicion de pago
	Recargo = 0.00 #recargo por la condicion de pago
	Bonificacion = 0.00 #bonificacion del cliente
	PrecioSIVA = 0.00 #precio sin iva
	Flete = 0.00 #flete del producto
	DescProd = 0.00 #monto de descuento aplicado al producto
	Precio = 0.00 #precio final del producto 
	Clave = '' #clave del producto
	bd = relaciones.Relaciones() #contiene todos los metodos para consulta y escritura a la base de datos
	Data = None #contiene todos los datos del producto luego de consultar a la base de datos
	CalculaReparto = False #calcula reparto o no
	Introduccion = 0.00 #introduccion de mercaderia en la localidad
	loc = None #datos de la localidad
	CalculaRecargo = False #se calcula el recargo del cliente para efectuar la venta
	CalculaIVA = False #si se calcula el iva
	CalculaImpuestos = False #para saber si debe calcular impuestos
	Impuestos = 0.00 #monto de los impuestos calculados
	CantDecimales = 4
	
	def ActualizaPrecio(self):
		
		self.bd.diccionario = True
		if self.loc is None:
			consulta = "select * from localidad where codigo = '" + globalDef.glb_locrep + "'"
			self.loc = self.bd.ConsultaUno(consulta)
			
		consulta = "select * from lista where codigo = '" + self.Clave + "'"
		self.Data = self.bd.ConsultaUno(consulta)
		
		self.PrecioBase()

		self.BoniCli()
		self.Precio = self.PrecioSIVA + self.PrecioSIVA * self.Recargo / 100. - self.PrecioSIVA * self.Descuento / 100.
		
		self.Precio = self.Precio - self.Precio * self.Bonificacion / 100.
		self.RepartoProd()

		self.IntroduccionProd()
		self.CalculaDescuento()

		self.Precio += self.Flete + self.Introduccion - self.Descuento

		if self.CalculaRecargo:
			self.Precio += self.Precio * self.Data['recargo'] / 100
		
		self.PrecioSIVA = round(self.Precio, self.CantDecimales)
		
		if self.CalculaIVA:
			self.CalcImp()
			self.Precio += self.Impuestos
		
		self.Precio = round(self.Precio, self.CantDecimales)
			
		self.bd.diccionario = False
	
	def BoniCli(self):
		self.Bonificacion = 0.00
		consulta = "select * from descuento where cliente = '" + globalDef.glb_cliente + "'"
		data = self.bd.ConsultaTodo(consulta)
		
		for d in data:
			if self.Clave >= d[2] and self.Clave <= d[3]:
				self.Bonificacion = d[4]
		
	def PrecioBase(self):
		if self.CalculaReparto:
			if globalDef.glb_lista == '1':
				self.PrecioSIVA = self.Data['pbl1rep']
			else:
				self.PrecioSIVA = self.Data['pbl4rep']
		else:
			if globalDef.glb_lista == '1':
				self.PrecioSIVA = self.Data['pbl1ret']
			else:
				self.PrecioSIVA = self.Data['pbl4ret']


	def RepartoProd(self):
		self.Flete = 0.00
		if self.Data['tiporeparto'] == 'P':
			if self.CalculaReparto:
				cIndice = 'fletep' + globalDef.glb_lista
				self.Flete = self.PrecioSIVA * self.loc[cIndice] / 100
			else:
				self.Flete = 0.00
		elif self.Data['tiporeparto'] == 'T':
			cIndice = 'fletetn' + globalDef.glb_lista
			self.Flete = self.loc[cIndice] * self.Data['peso'] / 1000
		else:
			self.Flete = 0.00
	
	
	def IntroduccionProd(self):
		self.Introduccion = 0.00
		if self.Data['tiporeparto'] == 'P':
			if self.CalculaReparto:
				cIndice = 'intporl' + globalDef.glb_lista
				self.Introduccion = self.PrecioSIVA * self.loc[cIndice] / 100
			else:
				self.Flete = 0.00
		elif self.Data['tiporeparto'] == 'T':
			cIndice = 'inttnl' + globalDef.glb_lista
			self.Introduccion = self.loc[cIndice] * self.Data['peso'] / 1000
		else:
			self.Introduccion = 0.00
	
	def CalculaDescuento(self):
		self.Descuento = 0.00
		if not self.CalculaReparto:
			cIndice = 'boni' + globalDef.glb_lista
			self.Descuento = self.PrecioSIVA * self.loc[cIndice] / 100
		else:
			self.Descuento = 0.00
			
	def CalcImp(self):
		info = self.bd.ConsultaUno("select * from info")
		
		nDGR = 0.00
		nMun = 0.00
		nIVA = self.Precio * self.Data['iva'] / 100
		if self.CalculaImpuestos:
			nDGR = self.Precio * info['dgr'] / 100
			nMun = self.Precio * info['otrosimp'] / 100
		
		self.Impuestos = nIVA + nDGR + nMun
			
		
if __name__ == "__main__":
	c = Calcula()
	c.Clave = '080.247'
	c.CalculaReparto = False
	c.Recargo = 0
	c.Descuento = 6.65
	c.CalculaIVA = True
	globalDef.glb_lista = '1'
	
	globalDef.glb_cliente = '00040'
	globalDef.glb_locrep = '0005'
	c.ActualizaPrecio()
	print "Precio cliente 00040 {}".format(c.Precio)
