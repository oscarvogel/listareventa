# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
from modelos import relaciones
from sistema import globalDef, CalculaPrecios
from vistas import CargaCant
from datetime import date

###########################################################################
## Class Ppal
###########################################################################

class Ppal ( wx.Frame ):
	
	fila, filadet 	= 0, 0
	col, coldet 	= 0, 0
	itemsgrilla = {}
	cantfilas = 0
	condicion = ""
	busqueda = "" #guarda los caracteres presionados
	
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 944,602 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		SizerPpal = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 2, 0, 0, 0 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Articulos para la venta" ), wx.VERTICAL )
		
		self.grdArt = wx.grid.Grid( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdArt.CreateGrid( 50, 5 )
		self.grdArt.EnableEditing( False )
		self.grdArt.EnableGridLines( True )
		self.grdArt.EnableDragGridSize( False )
		self.grdArt.SetMargins( 0, 0 )
		
		# Columns
		self.grdArt.EnableDragColMove( False )
		self.grdArt.EnableDragColSize( True )
		self.grdArt.SetColLabelSize( 30 )
		self.grdArt.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdArt.EnableDragRowSize( True )
		self.grdArt.SetRowLabelSize( 80 )
		self.grdArt.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdArt.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer1.Add( self.grdArt, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Articulos a vender" ), wx.VERTICAL )
		
		self.grdDet = wx.grid.Grid( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDet.CreateGrid( 0, 6 )
		self.grdDet.EnableEditing( False )
		self.grdDet.EnableGridLines( True )
		self.grdDet.EnableDragGridSize( False )
		self.grdDet.SetMargins( 0, 0 )
		
		# Columns
		self.grdDet.EnableDragColMove( False )
		self.grdDet.EnableDragColSize( True )
		self.grdDet.SetColLabelSize( 30 )
		self.grdDet.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdDet.EnableDragRowSize( True )
		self.grdDet.SetRowLabelSize( 80 )
		self.grdDet.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		#definimos los campos que contendra el grid
		self.grdDet.SetColLabelValue(0, 'Codigo')
		self.grdDet.SetColLabelValue(1, 'Unidad')
		self.grdDet.SetColLabelValue(2, 'Detalle')
		self.grdDet.SetColLabelValue(3, 'Cantidad')
		self.grdDet.SetColLabelValue(4, 'Precio')
		self.grdDet.SetColLabelValue(5, 'Total')
		
		# Cell Defaults
		self.grdDet.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sbSizer3.Add( self.grdDet, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer1.Add( sbSizer3, 1, wx.EXPAND, 5 )
		
		
		SizerPpal.Add( gSizer1, 1, wx.EXPAND, 0 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Sub Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.txtSubTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txtSubTotal.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.txtSubTotal.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.txtSubTotal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer7.Add( self.txtSubTotal, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"IVA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.txtIVA = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txtIVA.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.txtIVA.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.txtIVA.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer7.Add( self.txtIVA, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Percepcion DGR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.txtPercepcionDGR = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txtPercepcionDGR.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.txtPercepcionDGR.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.txtPercepcionDGR.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer7.Add( self.txtPercepcionDGR, 0, wx.ALL, 5 )
		
		self.Total = wx.StaticText( self, wx.ID_ANY, u"Total", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Total.Wrap( -1 )
		self.Total.SetFont( wx.Font( 12, 70, 90, 90, False, wx.EmptyString ) )
		bSizer7.Add( self.Total, 0, wx.ALL, 5 )
		
		self.txtTotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txtTotal.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		self.txtTotal.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		self.txtTotal.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer7.Add( self.txtTotal, 0, wx.ALL, 5 )
		
		
		SizerPpal.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnGraba = wx.Button( self, wx.ID_ANY, u"&Graba", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnGraba, 1, wx.ALL, 5 )
		
		self.btnSalir = wx.Button( self, wx.ID_ANY, u"&Salir", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnSalir, 1, wx.ALL, 5 )
		
		
		SizerPpal.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( SizerPpal )
		self.Layout()
		self.SatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.grdArt.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.grdArtOnGridSelectCell )
		self.grdArt.Bind( wx.EVT_KEY_DOWN, self.grdArtOnKeyDown )
		self.grdDet.Bind( wx.EVT_KEY_DOWN, self.grdDetOnKeyDown )
		self.grdDet.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.grdDetOnGridSelectCell )
		self.btnGraba.Bind( wx.EVT_BUTTON, self.btnGrabaOnButtonClick )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.btnSalirOnButtonClick )
		
		
		#inicializaciones varias
		self._bd = relaciones.Relaciones()
		self.calcula = CalculaPrecios.Calcula()
		self.ArmaGrillaArt()
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def grdArtOnKeyDown( self, event ):
		keycode = event.GetKeyCode()
		
		if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER:
			form = CargaCantidad(self)
			self.detalle	= self.grdArt.GetCellValue(self.fila, 2)
			self.unidad 	= self.grdArt.GetCellValue(self.fila, 1)
			self.precio		= float( self.grdArt.GetCellValue(self.fila, 4) )
			self.codigo		= self.grdArt.GetCellValue(self.fila, 0)
			form.unidad = self.unidad
			form.valor = self.codigo
			form.lblTitulo.SetLabel(self.detalle)
			form.lblUnidad.SetLabel(self.unidad)
			
			form.ShowModal()
			if globalDef.DEBUG: print "Cantidad retornada {}".format(form.cantidad)
			
			self.cantidad = form.cantidad
			form.Close()
			self.CargaGrilla()
		elif ( keycode >= wx.WXK_SPACE and keycode <= 168 ) or ( keycode >= wx.WXK_NUMPAD0 and keycode <= wx.WXK_NUMPAD9 ):
			print keycode
			
			#en caso de que sea el teclado numerico tengo que descontar 276 para llegar a un caracter ascii valido
			if keycode >= wx.WXK_NUMPAD0 and keycode <= wx.WXK_NUMPAD9:
				self.busqueda += chr( keycode - 276 )
			else:
				self.busqueda += chr( keycode )
				
				
			if self.col == 0:
				self.condicion = " and codigo like '%{clave}%'".format( clave = self.busqueda )
			elif self.col == 2:
				self.condicion = " and detalle like '%{clave}%'".format( clave = self.busqueda )
			else:
				self.condicion = ""
			
			if globalDef.DEBUG: print "Condicion de busqueda {}".format(self.condicion)
			self.ArmaGrillaArt()
		
		elif keycode == wx.WXK_BACK:
			#borro un caracter
			self.busqueda = self.busqueda[:-1]
			self.ArmaGrillaArt()
			
		elif keycode == wx.WXK_LEFT or wx.WXK_RIGHT:
			self.condicion = ""
			
		self.StatusBar.SetStatus(self.busqueda)
		event.Skip()
	
	def grdDetOnKeyDown( self, event ):
		keycode = event.GetKeyCode()
		grid = self.grdDet
		
		if keycode == wx.WXK_DELETE:
			grid.DeleteRows( self.filadet )
			del self.itemsgrilla[ self.filadet ]
			self.cantfilas -= 1
			self.Recalcula()
			
		event.Skip()
	
	
	def btnGrabaOnButtonClick( self, event ):
		fecha = date.today()
		
		query = """
			SELECT max(numero) as numero FROM cabrem where tipo = 'Z'
		"""
		data = self._bd.ConsultaUno(query)
		
		if globalDef.DEBUG: print "Maximo numero {}".format(data[0])
		if data[0] is None:
			numero = '000100000001'
		else:
			numero = str( int( data[0] ) + 1 ).zfill(12)
			
		query = """
			insert into cabrem
				(fecha, cliente, tipo, numero, neto, iva, dgr)
				values(?, ?, ?, ?, ?, ?, ?)
		"""
		parametros = [fecha.strftime("%Y%m%d"), 1, 'Z', numero, self.txtSubTotal.GetValue(), \
						self.txtIVA.GetValue(), self.txtPercepcionDGR.GetValue()]
		self._bd.EjecutaSQL(query, parametros)
		
		query = """
			select max(id) as id from cabrem
		"""
		ult = self._bd.ConsultaUno(query)
		
		if globalDef.DEBUG: print "Ultimo {}".format(ult)
		for i, j in self.itemsgrilla.iteritems():
			query = """
				insert into detrem
					(idCabRem, codigo, unidad, cantidad, unitario, iva, dgr, detalle)
					values(?, ?, ?, ?, ?, ?, ?, ?)
			"""
			parametros = [ult['id'], j['codigo'], j['unidad'], j['cantidad'], j['unitario'], j['iva'], j['dgr'], j['detalle']]
			
			if globalDef.DEBUG: print "Parametros {}, consulta {}".format(parametros, query)
			self._bd.EjecutaSQL(query, parametros)
		
		self.Close()
		event.Skip()
	
	def btnSalirOnButtonClick( self, event ):
		self.Close()
	
	def ArmaGrillaArt(self):
		grid = self.grdArt
		self._bd.diccionario = True
		
		consulta = "select * from pagos where pago = '" + globalDef.glb_condpago + "'"
		pagos = self._bd.ConsultaUno(consulta)
		
		self.calcula.Recargo = pagos['punitorio']
		self.calcula.Descuento = pagos['des1']
		self.calcula.CalculaIVA = True
		self.calcula.CalculaReparto = True
		self.calcula.CalculaRecargo = True
		
		consulta = "select codigo, unidad, detalle, preciopub, reducida, recargo "\
				"from lista "\
				"where reducida = 'S' {condicion}"\
				"limit 50".format(condicion = self.condicion)
		data = self._bd.ConsultaTodo(consulta)

		grid = self.grdArt
		numFilas = grid.GetNumberRows()
		numCols = grid.GetNumberCols()
		
		grid.ClearGrid()
		actual, nuevo = (numFilas, len(data))
        
		if nuevo < actual:
			#- Borro filas:
			grid.DeleteRows(0, actual - nuevo, True)
		
		if nuevo < 50: #en caso de que no haya 100 filas los establezco
			nuevo = 50
			
		if nuevo > actual:
			#- agrego filas:
			grid.AppendRows(nuevo - actual)

		#definimos los campos que contendra el grid
		grid.SetColLabelValue(0, 'Codigo')
		grid.SetColLabelValue(1, 'Unidad')
		grid.SetColLabelValue(2, 'Detalle')
		grid.SetColLabelValue(3, 'Precio S/IVA')
		grid.SetColLabelValue(4, 'Precio C/IVA')
		
		# Añadimos los campos de la base de datos a las columnas
		for i in range(0,len(data)):
			grid.SetCellValue(i,0,"%s" % data[i][0])
			grid.SetCellValue(i,1,"%s" % data[i][1])
			grid.SetCellValue(i,2,"%s" % data[i][2])
			
			self.calcula.Clave = data[i][0]
		
			self.calcula.ActualizaPrecio()
			
			grid.SetCellValue(i,3,"%s" % self.calcula.PrecioSIVA)
			
			grid.SetCellValue(i,4,"%s" % self.calcula.Precio)

		grid.AutoSizeColumns()
		grid.Refresh()


	def grdArtOnGridSelectCell(self, event):
		self.fila = event.GetRow()
		self.col = event.GetCol()
		event.Skip()
	
	def grdDetOnGridSelectCell( self, event ):
		self.filadet = event.GetRow()
		self.coldet = event.GetCol()
		event.Skip()
	
	def CargaGrilla(self):
		grid = self.grdDet
		#agregamos una fila
		grid.AppendRows(1)
		
		if globalDef.DEBUG: print "Tipo cantidad {}, tipo precio {} ".format(type(self.cantidad), type(self.precio))
		
		grid.SetCellValue(self.cantfilas,0,"%s" % self.codigo)
		grid.SetCellValue(self.cantfilas,1,"%s" % self.unidad)
		grid.SetCellValue(self.cantfilas,2,"%s" % self.detalle)
		grid.SetCellValue(self.cantfilas,3,"%s" % self.cantidad)
		grid.SetCellValue(self.cantfilas,4,"%s" % self.precio)
		grid.SetCellValue(self.cantfilas,5,"%s" % str( self.cantidad * self.precio ) )
		
		self.itemsgrilla[self.cantfilas] = dict([('codigo', self.codigo), ('cantidad', self.cantidad), ( 'iva', 0.0000 ), ( 'unitario', self.precio ), \
											( 'dgr', 0.00 ), ( 'unidad', self.unidad ), ( 'detalle', self.detalle ) ])

		#incrementamos en uno la cantidad total de filas
		self.cantfilas += 1
		
		#recalculamos los totales
		self.Recalcula()
		grid.AutoSizeColumns()
		grid.Refresh()
		
	
	
	def Recalcula(self):
		
		self._bd.diccionario = True
		
		consulta = "select * from pagos where pago = '" + globalDef.glb_condpago + "'"
		pagos = self._bd.ConsultaUno(consulta)
		
		self.calcula.Recargo = pagos['punitorio']
		self.calcula.Descuento = pagos['des1']
		self.calcula.CalculaIVA = True
		self.calcula.CalculaReparto = True
		self.calcula.CalculaRecargo = True
		
		nTotIVA = 0.00
		nNeto = 0.00
		for i, j in self.itemsgrilla.iteritems():
			self.calcula.Clave = j['codigo']
			self.calcula.ActualizaPrecio()
			j['iva'] = ( self.calcula.Precio - self.calcula.PrecioSIVA ) * j['cantidad']
			nTotIVA += j['iva']
			nNeto += self.calcula.PrecioSIVA * j['cantidad']
			if globalDef.DEBUG: print "precio con iva {} precio sin iva {}".format(self.calcula.Precio, self.calcula.PrecioSIVA)
			
		self.txtSubTotal.SetValue( str( nNeto ) )
		self.txtIVA.SetValue( str( nTotIVA ) )
		self.txtTotal.SetValue( str( nNeto + nTotIVA ) )
		
		
	
class CargaCantidad(CargaCant.Ppal):
	
	valor = None
	unidad = None
	campoa1 = None
	peso = 0.00
	mts2 = 0.00
	espesor = 0.00
	cantidad = 0.00
	# Virtual event handlers, overide them in your derived class
	def PpalOnInitDialog( self, event ):
		self.txtCantidad.SetValue('1')
		self._bd = relaciones.Relaciones()
		self._bd.diccionario = True
		consulta = "select * from lista where codigo = '" + self.valor + "'"
		data = self._bd.ConsultaUno(consulta)
		
		self.campoa1 = data['campoa1']
		self.peso = float( data['peso'] )
		self.mts2 = float( data['mts2'] )
		self.espesor = float( data['espesor'] )
		if data['campoa1'] == 'C':
			self.lblCajas.SetLabel(u"Peso")
		elif data['campoa1'] == 'A' and data['mts2'] != 0:
			self.lblCajas.SetLabel(u'Cajas')
		elif data['campoa1'] == 'M':
			self.lblCajas.SetLabel(u'Mts. Lin.')
		elif data['campoa1'] == 'S':
			self.lblCajas.SetLabel(u'Sup. M2')
			
		event.Skip()
	
	def txtCantidadOnKillFocus( self, event ):
		valor = float(self.txtCantidad.GetValue())
		
		if self.campoa1 == 'M':
			if self.peso != 0:
				self.txtCajas.SetValue( str(valor / self.peso) )
		elif self.campoa1 == 'A':
			nCaj = round( valor / self.mts2,2 )
			if nCaj % 1 != 0:
				self.txtCajas.SetValue( str( int( nCaj + 1 ) ) )
				nCajas = int(nCaj + 1)
				if globalDef.DEBUG: print "nCaj {} nCajas {}".format( nCaj, nCajas )
			else:
				self.txtCajas.SetValue( str( int( nCaj ) ) )
				nCajas = int( nCaj )
			
			self.txtCantidad.SetValue( str( int( nCajas ) * self.mts2) )
			self.txtDescripcion.SetValue( u"{} CAJAS DE {} MTS2".format(nCajas, self.mts2 ))
		elif self.campoa1 == 'S':
			self.txtCajas.SetValue( valor / self.espesor / 8 )
		else:
			self.txtCajas.SetValue( str(valor * self.peso) )
		
		self.cantidad = float( self.txtCantidad.GetValue( ) )
		event.Skip()
	
	def txtCajasOnKillFocus( self, event ):
		event.Skip()
	
	def btnAceptarOnButtonClick( self, event ):
		self.Close(True) 
		self.MakeModal(False)
		self.Destroy()
		return self.cantidad
	
	def btnCerrarOnButtonClick( self, event ):
		self.Close()
	
	def txtCantidadOnChar( self, event ):
		keycode = event.GetKeyCode()
		
		if keycode == wx.WXK_RETURN:
			self.btnAceptar.SetFocus()
		
		event.Skip()
		
	def txtCajasOnChar( self, event ):
		event.Skip()
	
		keycode = event.GetKeyCode()
		
		if keycode == wx.WXK_RETURN:
			self.btnAceptar.SetFocus()
		
		event.Skip()
	
	
	def txtCantidadOnKeyUp( self, event ):
		event.Skip()

