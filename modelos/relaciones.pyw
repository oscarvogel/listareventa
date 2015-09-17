#! /usr/bin/python
#encoding:utf-8

from sistema import conectarBD
import MySQLdb as my, sqlite3 as lite

class Relaciones(object):
	
	tipo = None
	#atributo que indica si debe devolver las filas como diccionario
	diccionario = None
	
	
	def CreaTablas(self):
		self.CreaInfo()
		self.CreaClientes()
		self.CreaLocalidad()
		self.CreaPagos()
		self.CreaLista()
		self.CreaVariacion()
		self.CreaDescuento()
		self.CreaCabRem()
		self.CreaDetRem()
		
		
	def ConsultaTodo(self, consulta = '', parametros = None):
		
		if consulta == '':
			return None
			
		bd = conectarBD.ConectarBD(self.tipo)

		if self.diccionario:
			if self.tipo is None:
				bd.get_bd().row_factory = lite.Row
				cur = bd.get_bd().cursor()
			else:
				cur = bd.get_bd().cursor(my.cursors.DictCursor)
		else:
			cur = bd.get_bd().cursor()
		
		if parametros is None:
			cur.execute(consulta)
		else:
			cur.execute(consulta, parametros)
			
		filas = cur.fetchall()
		cur.close()
		bd.get_bd().close()
		return filas 
	
	
	def ConsultaUno(self, consulta = ''):
		if consulta == '':
			return None

		bd = conectarBD.ConectarBD(self.tipo)
		
		if self.diccionario:
			if self.tipo is None:
				bd.get_bd().row_factory = lite.Row
				cur = bd.get_bd().cursor()
			else:
				cur = bd.get_bd().cursor(my.cursors.DictCursor)
		else:
			cur = bd.get_bd().cursor()

		cur.execute(consulta)
		fila = cur.fetchone()
		cur.close()
		bd.get_bd().close()
		
		return fila
		
	def EjecutaSQL(self, query = '', parametros = None):
		if query == '':
			return None
		
		bd = conectarBD.ConectarBD(self.tipo)
		
		if self.diccionario:
			if self.tipo is None:
				bd.get_bd().row_factory = lite.Row
				cur = bd.get_bd().cursor()
			else:
				cur = bd.get_bd().cursor(my.cursors.DictCursor)
		else:
			cur = bd.get_bd().cursor()
		
		if parametros is None:
			cur.execute(query)
		else:
			cur.execute(query, parametros)
		
		cur.close()
		bd.get_bd().commit()
		bd.get_bd().close()

		
	def CreaInfo(self):
		
		if not self.ExisteTabla('info'):
			query = "create table info (codigo char(10), fecha date, email varchar(150))"
			self.EjecutaSQL(query)
			query = "insert into info (codigo, fecha, email) values('', '', '')"
			self.EjecutaSQL(query)

		if not self.ExisteCampoTabla('info', 'dgr'):
			query = "alter table info add column dgr char(6)"
			self.EjecutaSQL(query)

		if not self.ExisteCampoTabla('info', 'iva'):
			query = "alter table info add column iva char(6)"
			self.EjecutaSQL(query)

		if not self.ExisteCampoTabla('info', 'otrosimp'):
			query = "alter table info add column otrosimp char(6)"
			self.EjecutaSQL(query)
	
	
	def ExisteTabla(self, cTabla = ''):
		
		if cTabla == '':
			return False
		
		consulta = "SELECT name FROM sqlite_master WHERE TYPE='table' AND name='" + cTabla + "'"
		data = self.ConsultaUno(consulta)
		
		if data is None:
			return False
		else:
			return True 
	
	def EncuentraClave(self, cTabla = '', cCampo = '', cValor = ''):
		
		query = "select * from " + cTabla + " where " + cCampo + " = '" + cValor + "'"
		data = self.ConsultaUno(query)
		if data is None:
			return False
		else:
			return True
		
	def ExisteCampoTabla(self, cTabla = '', cCampo = ''):
		if cTabla == '' or cCampo == '':
			return False
			
		consulta = "pragma table_info('" + cTabla + "')"
		
		data = self.ConsultaTodo(consulta)
		
		lRetorno = False
		for d in data:
			if d[1].upper() == cCampo.upper():
				lRetorno = True
		
		return lRetorno
			
	def CreaClientes(self):
		
		if not self.ExisteTabla('clientes'):
			query = """
				create table clientes
					(codigo char(10), lista char(1), nombre char(40), localidad char(4), pago char(2))
			"""
			self.EjecutaSQL(query)
			
	def CreaLocalidad(self):
		
		if not self.ExisteTabla('localidad'):
			query = """
				create table localidad
					(codigo char(4) primary key, nombre char(50), distancia decimal(5), provincia char(20), codpos char(8),
					fletep1 real, fletetn1 real, fletep4 real, fletetn4 real, boni1 real, boni4 real, zona char(1),
					reparto char(1), inttnl1 real, inttnl4 real, intporl1 real, intporl4 real)
			"""
			self.EjecutaSQL(query)
	
	def CreaPagos(self):
		if not self.ExisteTabla("pagos"):
			query = """
				create table pagos
					(pago char(2), detalle char(30), lista char(1), punitorio real, des1 real, dia date,
					tipo char(1))
			"""
			self.EjecutaSQL(query)
		
	def CreaLista(self):
		if not self.ExisteTabla("lista"):
			query = """
				create table lista
					(codigo char(8), unidad char(8), detalle char(40), peso real, espesor real, iva real,
					mts2 real, precio1 real, precio4 real, reparto char(2), redferre char(1), tiporeparto char(1),
					campoa1 char(1), reducida char(1), preciopub real, recargo real, estado char(1), pbl1ret real,
					pbl4ret real, pbl1rep real, pbl4rep real)
			"""
			self.EjecutaSQL(query)
			
			query = "create unique index principal on lista (codigo)"
			self.EjecutaSQL(query)
			
			query = """
				CREATE TRIGGER up_lista AFTER UPDATE 
					ON lista WHEN new.precio1 <> old.precio1 or new.precio4 <> old.precio4
					BEGIN
						insert into variacion
							(codigo, unidad, detalle, precioantl1, precioactl1, precioantl4, 
								precioactl4, fechaact)
							values( new.codigo, new.unidad, new.detalle, old.precio1, new.precio1, 
								old.precio4, new.precio4, date());
						update lista set estado = 'M' where codigo = new.codigo;
					END;
			"""
			self.EjecutaSQL(query)
			
	def CreaVariacion(self):
		if not self.ExisteTabla("variacion"):
			query = """
				create table variacion
					(codigo char(8), unidad char(8), detalle char(40), precioantl1 real, precioactl1 real, 
					precioantl4 real, precioactl4 real, fechaact date )
			"""
			self.EjecutaSQL(query)


	def CreaDescuento(self):
		if not self.ExisteTabla("descuento"):
			query = """
				create table descuento
					(id int, cliente char(5), desdeart char(8), hastaart char(8), descuento real)
			"""
			self.EjecutaSQL(query)
			
			query = "create unique index ppaldesc on descuento (id)"
			self.EjecutaSQL(query)
	
	def CreaCabRem(self):
		if not self.ExisteTabla("cabrem"):
			query = """
				create table cabrem
					(id INTEGER PRIMARY KEY AUTOINCREMENT, fecha date, cliente int, tipo char(1), numero char(12), 
					neto real, iva real, dgr real)
			"""
			self.EjecutaSQL(query)
			
	def CreaDetRem(self):
		if not self.ExisteTabla("detrem"):
			query = """
				create table detrem
					(id INTEGER PRIMARY KEY AUTOINCREMENT, idCabRem int, codigo char(8), unidad char(8), cantidad real,
					unitario real, iva real, dgr real, detalle char(40) )
			"""
			self.EjecutaSQL(query)
