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
from sistema import CalculaPrecios
from sistema import globalDef, funciones

###########################################################################
## Class Lista
###########################################################################

class Lista ( wx.Frame ):
	
	cOrden = ''
	SeleccionGrilla = None
	cReducida = ''
	desde = None
	hasta = None
	
	def __init__( self, parent, ListaReducida = '' ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 883,558 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.cReducida = ListaReducida
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Busqueda", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.txtBusqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.txtBusqueda, 1, wx.ALL, 5 )
		
		cboEntregaChoices = [ u"Reparto", u"Retira" ]
		self.cboEntrega = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cboEntregaChoices, 0 )
		self.cboEntrega.SetSelection( 0 )
		bSizer4.Add( self.cboEntrega, 0, wx.ALL, 5 )
		
		cboIVAChoices = [ u"Con IVA", u"Sin IVA" ]
		self.cboIVA = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cboIVAChoices, 0 )
		self.cboIVA.SetSelection( 0 )
		bSizer4.Add( self.cboIVA, 0, wx.ALL, 5 )
		
		self.btnOrdenAlf = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/OrdenAlfabetico.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4.Add( self.btnOrdenAlf, 0, wx.ALL, 5 )
		
		self.btnOrdenNum = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/OrdenNumerico.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4.Add( self.btnOrdenNum, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.lblOrden = wx.StaticText( self, wx.ID_ANY, u"Orden establecido:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblOrden.Wrap( -1 )
		bSizer51.Add( self.lblOrden, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Lista Reducida", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText3.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer51.Add( self.m_staticText3, 0, wx.ALL, 5 )

		bSizer3.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.grdDatos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDatos.CreateGrid( 20, 5 )
		self.grdDatos.EnableEditing( True )
		self.grdDatos.EnableGridLines( True )
		self.grdDatos.EnableDragGridSize( False )
		self.grdDatos.SetMargins( 0, 0 )
		
		# Columns
		self.grdDatos.SetColSize( 0, 109 )
		self.grdDatos.SetColSize( 1, 112 )
		self.grdDatos.SetColSize( 2, 247 )
		self.grdDatos.SetColSize( 3, 140 )
		self.grdDatos.EnableDragColMove( False )
		self.grdDatos.EnableDragColSize( True )
		self.grdDatos.SetColLabelSize( 30 )
		self.grdDatos.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.grdDatos.EnableDragRowSize( True )
		self.grdDatos.SetRowLabelSize( 80 )
		self.grdDatos.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.grdDatos.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer5.Add( self.grdDatos, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnExcel = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/excel2007_d.JPG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnExcel.SetBitmapSelected( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		self.btnExcel.SetBitmapFocus( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		self.btnExcel.SetBitmapHover( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		self.btnExcel.SetToolTipString("Exporta los datos a Excel")
		bSizer6.Add( self.btnExcel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnAgregar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/document-new-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnAgregar.SetBitmapDisabled( wx.Bitmap( u"graphics/document-new-b.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetBitmapSelected( wx.Bitmap( u"graphics/document-new.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetBitmapFocus( wx.Bitmap( u"graphics/document-new.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetBitmapHover( wx.Bitmap( u"graphics/document-new.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetToolTipString("Agrega a lista reducida")
		bSizer6.Add( self.btnAgregar, 1, wx.ALL, 5 )
		
		self.btnSalir = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/LogOut-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnSalir.SetBitmapSelected( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapFocus( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapHover( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetToolTipString("Cierra formulario")
		bSizer6.Add( self.btnSalir, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		self.calcula = CalculaPrecios.Calcula()
		self.__relaciones__ = relaciones.Relaciones()
		self.__funciones__ = funciones.Funciones()
		
		self.__relaciones__.diccionario = True
		consulta = "select * from localidad where codigo = '" + globalDef.glb_locrep + "'"
		self.loc = self.__relaciones__.ConsultaUno(consulta)

		self.CalculaIVA = True
		self.CalculaReparto = True
		self.ArmaGrilla()
		
		# Connect Events
		self.txtBusqueda.Bind( wx.EVT_KEY_UP, self.txtBusquedaOnKeyUp )
		self.cboEntrega.Bind( wx.EVT_CHOICE, self.cboEntregaOnChoice )
		self.cboIVA.Bind( wx.EVT_CHOICE, self.cboIVAOnChoice )
		self.btnOrdenAlf.Bind( wx.EVT_BUTTON, self.btnOrdenAlfOnButtonClick )
		self.btnOrdenNum.Bind( wx.EVT_BUTTON, self.btnOrdenNumOnButtonClick )
		self.btnExcel.Bind( wx.EVT_BUTTON, self.btnExcelOnButtonClick )
		self.btnAgregar.Bind( wx.EVT_BUTTON, self.btnAgregarOnButtonClick )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.btnSalirOnButtonClick )
		self.grdDatos.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.grdDatosOnGridSelectCell )
		self.grdDatos.Bind( wx.grid.EVT_GRID_CELL_CHANGE, self.grdDatosOnGridCellChange )
		self.grdDatos.Bind( wx.grid.EVT_GRID_RANGE_SELECT, self.grdDatosOnGridRangeSelect )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtBusquedaOnKeyUp( self, event ):
		self.ArmaGrilla()
		event.Skip()
	
	def cboEntregaOnChoice( self, event ):
		
		if event.GetString() == u"Reparto":
			self.CalculaReparto = True
		else:
			self.CalculaReparto = False
			
		event.Skip()
	
	def cboIVAOnChoice( self, event ):
		if event.GetString() == 'Con IVA':
			self.CalculaIVA = True
		else:
			self.CalculaIVA = False
		event.Skip()
	
	def btnOrdenAlfOnButtonClick( self, event ):
		self.cOrden = 'A'
		self.ArmaGrilla()
		event.Skip()
	
	def btnOrdenNumOnButtonClick( self, event ):
		self.cOrden = 'N'
		self.ArmaGrilla()
		event.Skip()
	
	def btnExcelOnButtonClick( self, event ):
		self.ExportaExcel()
		event.Skip()
	
	def btnAgregarOnButtonClick( self, event ):
		
		if self.desde != None and self.hasta != None:
			for i in range(self.desde, self.hasta + 1):
				value = self.grdDatos.GetCellValue(i, 0)
				self.SeleccionGrilla = value
				self.CambiaEstado()
		else:
			self.CambiaEstado()
		
		self.ArmaGrilla()
		self.desde = None
		self.hasta = None
		event.Skip()
	
	def btnSalirOnButtonClick( self, event ):
		self.Close()
	
	def grdDatosOnGridSelectCell( self, event ):
		row, col = event.GetRow(), event.GetCol()
		value = self.grdDatos.GetCellValue(row, 0)
		if self.grdDatos.GetCellValue(row, 4) == 'S':
			self.btnAgregar.SetToolTipString("Elimina de lista reducida")
		else:
			self.btnAgregar.SetToolTipString("Agrega a lista reducida")
			
		self.SeleccionGrilla = value
		event.Skip()
		
	def grdDatosOnGridCellChange(self, event):
		row, col = event.GetRow(), event.GetCol()
		value = self.grdDatos.GetCellValue(row, col)
		codigo = self.grdDatos.GetCellValue(row, 0)
		if col == 4:
			query = "update lista set recargo = " + value + " where codigo = '" + codigo + "'"
			self.__relaciones__.EjecutaSQL(query)
		
		
	def ArmaGrilla(self):
		
		self.__relaciones__.diccionario = True
		consulta = "select * from pagos where pago = '" + globalDef.glb_condpago + "'"
		pagos = self.__relaciones__.ConsultaUno(consulta)
		
		self.calcula.Recargo = pagos['punitorio']
		self.calcula.Descuento = pagos['des1']
		self.calcula.loc = self.loc
		self.calcula.CalculaIVA = self.CalculaIVA
		self.calcula.CalculaReparto = self.CalculaReparto
		
		query = "select codigo, unidad, detalle, preciopub, reducida, recargo from lista"
		
		if self.cReducida == 'S':
			query += " where reducida = 'S'"
		
		condicion = self.txtBusqueda.GetValue()
		if condicion != '':
			if query.find("where") == -1:
				query += " where "
			else:
				query += " and "

			if self.cOrden == "A":
				query += " detalle like '%" + condicion.upper() + "%'"
			else:
				query += " codigo like '%" + condicion + "%'"
				
		if self.cOrden == 'A':
			self.lblOrden.SetLabel(u"Orden establecido: NOMBRE")
			query += " order by detalle"
		else:
			self.lblOrden.SetLabel(u"Orden establecido: CODIGO")
			query += " order by codigo"
			
		query += " limit 50"
		
		self.data = self.__relaciones__.ConsultaTodo(query)
		
		data = self.data
		numFilas = self.grdDatos.GetNumberRows()
		numCols = self.grdDatos.GetNumberCols()
        
		grid = self.grdDatos
        
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
		grid.SetColLabelValue(3, 'Precio')
		if self.cReducida == 'S':
			grid.SetColLabelValue(4, 'Recargo')
		else:
			grid.SetColLabelValue(4, 'Reducida')
		
		# Añadimos los campos de la base de datos a las columnas
		for i in range(0,len(data)):
			grid.SetCellValue(i,0,"%s" % data[i][0])
			grid.SetCellValue(i,1,"%s" % data[i][1])
			grid.SetCellValue(i,2,"%s" % data[i][2])
			
			self.calcula.Clave = data[i][0]
		
			self.calcula.ActualizaPrecio()
			
			grid.SetCellValue(i,3,"%s" % self.calcula.Precio)
			
			if self.cReducida == 'S':
				grid.SetCellValue(i,4,"%s" % data[i][5])
			else:
				grid.SetCellValue(i,4,"%s" % data[i][4])
				
				if data[i][4] == 'S':
					attr = wx.grid.GridCellAttr()
					attr.SetTextColour(wx.BLACK)
					attr.SetBackgroundColour(wx.RED)
					grid.SetRowAttr(i, attr)
				else:
					attr = wx.grid.GridCellAttr()
					attr.SetTextColour(wx.BLACK)
					attr.SetBackgroundColour(wx.WHITE)
					grid.SetRowAttr(i, attr)
				

		
		grid.AutoSizeColumns()
		grid.Refresh()
		self.__relaciones__.diccionario = False
		

	def ExportaExcel(self):
		import xlsxwriter
		
		workbook = xlsxwriter.Workbook("actualizacion.xlsx")
		
		worksheet = workbook.add_worksheet('Actualizacion') 
		
		col = 0 
		row = 0
		worksheet.write(row, col, u'Codigo')
		worksheet.write(row, col + 1, u'Unidad')
		worksheet.write(row, col + 2, u'Detalle')
		worksheet.write(row, col + 3, u'Precio')
		worksheet.set_column(0, 0, 7.50)
		worksheet.set_column(1, 0, 7.50)
		worksheet.set_column(2, 0, 50)
		worksheet.set_column(3, 0, 7)
		
		format_number = workbook.add_format()
		format_number.set_num_format('###,##0.00')
		for codigo, unidad, detalle, precio in (self.data):
			worksheet.write(row, col,     codigo)
			worksheet.write(row, col + 1, unidad)
			worksheet.write(row, col + 2, detalle)
			
			self.calcula.Clave = codigo
		
			self.calcula.ActualizaPrecio()
			worksheet.write_number(row, col + 3, self.calcula.Precio, format_number)
			row += 1
			 
		workbook.close()
		self.__funciones__.Info(message = "Datos exportados a Excel", ventana = self)

	def grdDatosOnGridRangeSelect( self, event ):
		rowini, colini = event.GetTopLeftCoords()
		rowfin, colfin = event.GetBottomRightCoords()
	
		if event.Selecting():
			self.desde, self.hasta = rowini, rowfin
		
	def CambiaEstado(self):		
		
		if self.SeleccionGrilla is None:
			self.__funciones__.Info(message = "No hay ningun articulo seleccionado", ventana = self)
		else:
			self.__relaciones__.diccionario = True
			self.__relaciones__.tipo = None
			consulta = "select reducida from lista where codigo = '" + self.SeleccionGrilla + "'"
			data = self.__relaciones__.ConsultaUno(consulta)
			if data['reducida'] == 'S':
				query = "update lista set reducida = '' "
			else:
				query = "update lista set reducida = 'S' "
			
			query += " where codigo = '" + self.SeleccionGrilla + "'"
			self.__relaciones__.EjecutaSQL(query)
			self.SeleccionGrilla = None
