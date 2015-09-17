#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx
from os.path import join
from vistas import ListaReventa, Variaciones, Lista, ListaVenta
from modelos import pagos
from sistema import globalDef
from modelos import relaciones
from sistema import validaciones, funciones
from datetime import date

class Iniciar(ListaReventa.Ppal):
	
	info = False
	def Inicializar(self):

		self.lblTitulo.SetBackgroundColour('Red')
		
		self.__funciones__ = funciones.Funciones()
		self.__relaciones__ = relaciones.Relaciones()
		self.__relaciones__.CreaTablas()
		self.__busqueda__ = funciones.Selecciona(self)
		self.InfoBar.ShowMessage(msg="Presiona TAB para pasar de campo y F2 para ayuda de codigos")
		info = self.__relaciones__.ConsultaUno("select * from info")
		
		if not info is None:
			if info[0] != '':
				if info[0][-1] == '1':
					globalDef.glb_lista = '1'
				else:
					globalDef.glb_lista = '4'
				
				self.info = True
				self.CargaDatos()
			else:
				globalDef.glb_lista = '1'
		else:
			globalDef.glb_lista = '1'
					
		self.txtNroCliente.SetValidator(validaciones.ValidaCliente())

		self.txtNroCliente.SetFocus()
		
		
	def btnSalirOnButtonClick( self, event ):
		self.Close()
		
	def txtNroClienteOnKillFocus(self, event):
		
		if self.info:
			query = "update info set codigo = '" + self.txtNroCliente.GetValue().upper() + "'"
		else:
			query = "insert into info (codigo) values('" + self.txtNroCliente.GetValue().upper() + "')"
			self.info = True
		
		#numero de cliente de ferreteria
		globalDef.glb_cliente = self.txtNroCliente.GetValue().upper()[1:6]
		
		self.__relaciones__.EjecutaSQL(query)
		query = "select * from clientes where codigo = '" + self.txtNroCliente.GetValue().upper() + "'"
		data = self.__relaciones__.ConsultaUno(query)
		if data is None:
			self.__funciones__.Warn(ventana = self, message = "Cliente no encontrado en el sistema. Consulte a casa central")
			self.lblNombre.SetLabel('')
		else:
			self.lblNombre.SetLabel(data[2])
			self.txtLocalidad.SetValue(data[3])
			#cargo las condiciones de pago segun la lista del cliente
			datospagos = pagos.Pagos()
			codigos = datospagos.TraeDatos(data[1])
			
			for codigo in codigos:
				self.cboPago.Insert(codigo, codigos.index(codigo))
			
			consulta = "select * from pagos where pago = '" + data[4] + "'"
			datapago = self.__relaciones__.ConsultaUno(consulta)
			self.cboPago.SetValue(datapago[0] + '-' + datapago[1])
		
		globalDef.glb_locrep = self.txtLocalidad.GetValue()
		globalDef.glb_condpago = self.cboPago.GetValue()[0:2]
		event.Skip()
		
		
	def txtEmailOnKillFocus( self, event ):
		if self.info:
			query = "update info set email = '" + self.txtEmail.GetValue() + "'"
		else:
			query = "insert into info (email) values('" + self.txtNroCliente.GetValue() + "')"
			self.info = True
		self.__relaciones__.EjecutaSQL(query)
		event.Skip()
	
	def CargaDatos(self):
		consulta = "select * from info"
		data = self.__relaciones__.ConsultaUno(consulta)
		
		if data is None:
			self.info = False
		else:
			self.info = True
			self.txtNroCliente.SetValue(data[0])
			self.txtEmail.SetValue(data[2])
			if data[3] is None:
				self.txtDGR.SetValue('0')
			else:
				self.txtDGR.SetValue(data[3])
			
			if data[4] is None:
				self.optIVA.selection = 0
			else:
				if self.optIVA.FindString(data[4]) <> wx.NOT_FOUND:
					self.optIVA.SetSelection(self.optIVA.FindString(data[4]))
			
			if data[5] is None:
				self.txtOtrosImp.SetValue('0')
			else:
				self.txtOtrosImp.SetValue(data[5])
				
	def txtLocalidadOnKillFocus( self, event ):
		self.txtLocalidad.SetValue(self.txtLocalidad.GetValue().zfill(4))
		consulta = "select * from localidad where codigo = '" + self.txtLocalidad.GetValue() + "'"
		data = self.__relaciones__.ConsultaUno(consulta)
		
		if data is None:
			self.__funciones__.Warn(ventana = self, message = "Localidad no encontrado en el sistema")
			self.lblLocalidad.SetLabel('')
		else:
			self.lblLocalidad.SetLabel(data[1])
			
		globalDef.glb_locrep = self.txtLocalidad.GetValue()
		event.Skip()
	
	def txtLocalidadOnChar(self, event):
		keycode = event.GetKeyCode()
		
		if keycode == wx.WXK_F2:
			valor = self.__busqueda__.Buscar(ventana = self, tabla = "localidad")
			if valor <> self.txtLocalidad.GetValue() and valor <> '':
				self.txtLocalidad.SetValue(valor)
		elif keycode == wx.WXK_RETURN:
			self.cboPago.SetFocus()
				
		event.Skip()

	def cboPagoOnCombobox(self, event):
		valor = self.cboPago.GetValue()
		globalDef.glb_condpago = valor[0:2]
		print globalDef.glb_condpago
		
	def txtLocalidadOnSetFocus(self, event):
		self.InfoBar.ShowMessage(msg="Presiona TAB para pasar de campo y F2 para ayuda de codigos")
		event.Skip()
		
	def txtNroClienteOnChar(self, event):
		keycode = event.GetKeyCode()
		if wx.WXK_RETURN == keycode:
			try:
				self.optIVA.SetFocus()
			except:
				event.GetEventObject().GetPrevSibling().SetFocus()
		event.Skip()
		
		
	def optIVAOnChar(self, event):
		keycode = event.GetKeyCode()
		
		if wx.WXK_RETURN == keycode:
			self.txtDGR.SetFocus()
		event.Skip()
		
	def txtDGROnKillFocus(self, event):
		query = "update info set dgr = '" + self.txtDGR.GetValue() + "'"
		self.__relaciones__.EjecutaSQL(query)
		
	def txtDGROnChar(self, event):
		keycode = event.GetKeyCode()
		if wx.WXK_RETURN == keycode:
			self.txtOtrosImp.SetFocus()
			
		event.Skip()

	def optIVAOnChoice(self, event):
		query = "update info set iva = '" + event.GetString() + "'"
		self.__relaciones__.EjecutaSQL(query)
	
	def txtOtrosImpOnKillFocus(self, event):
		query = "update info set otrosimp = '" + self.txtOtrosImp.GetValue() + "'"
		self.__relaciones__.EjecutaSQL(query)
		
	def txtOtrosImpOnChar(self, event):
		keycode = event.GetKeyCode()
		if wx.WXK_RETURN == keycode:
			self.txtEmail.SetFocus()
		
		event.Skip()
	
	def cboPagoOnChar(self, event):
		keycode = event.GetKeyCode()
		if wx.WXK_RETURN == keycode:
			self.pagina2.SetFocus()
			
	def btnActualizaListaOnButtonClick(self, event):
		import cargastock, cargapagos, cargalocalidades, cargadescuentos
		import cargaclientes
		
		c = cargastock.CargaStock()
		c.ActualizaStock(ventana = self)
		
		c = cargapagos.CargaPagos()
		c.InsertaPagos(ventana = self)
		
		c = cargalocalidades.CargaLocalidades()
		c.InsertaLocalidades(ventana = self)
		
		c = cargadescuentos.CargaDescuentos()
		c.InsertaDescuentos(ventana = self)
		
		c = cargaclientes.CargaClientes()
		c.InsertaClientes(ventana = self)

		d = date.today()
		p = [d.strftime("%Y%m%d")]
		
		query = """
			update info set fecha = ?
		"""
		self.__relaciones__.EjecutaSQL(query, p)
	
	def btnVariacionesOnButtonClick( self, event ):
		form = Variaciones.Variaciones( self)
		form.Show(True)
		event.Skip()
	
	def btnListaGeneralOnButtonClick(self, event):
		form = Lista.Lista(self)
		form.Show(True)
		event.Skip()
	
	def btnListaReducidaOnButtonClick( self, event ):
		form = Lista.Lista(self, ListaReducida = 'S')
		form.Show(True)
		event.Skip()
		
	def btnVentasOnButtonClick( self, event ):
		form = ListaVenta.Ppal(self)
		form.itemsgrilla = {}
		form.Show(True)
		event.Skip()
		
class App(wx.App):
	
	def OnInit(self):
		try:
			frame = Iniciar(None)
			frame.Inicializar()
			frame.Show(True)
			return True
		except RuntimeError as err:
			print "Ha ocurrido un error y no podemos iniciar el sistema"
			print err
			return False


if __name__ == '__main__':
	app = App()
	app.MainLoop()
