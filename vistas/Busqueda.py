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

###########################################################################
## Class Ppal
###########################################################################

class Ppal ( wx.Dialog ):
	
	tabla = None
	campos = None
	CampoBusqueda = None
	ValorRetorno = ''
	
	def __init__( self, parent ):
		#wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 613,566 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 613,566 ), style = wx.DEFAULT_DIALOG_STYLE )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		#self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtBusqueda = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txtBusqueda, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.grdDatos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDatos.CreateGrid( 20, 0 )
		self.grdDatos.EnableEditing( False )
		self.grdDatos.EnableGridLines( False )
		self.grdDatos.EnableDragGridSize( False )
		self.grdDatos.SetMargins( 0, 0 )
		
		# Columns
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
		bSizer5.Add( self.grdDatos, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAceptar = wx.Button( self, wx.ID_ANY, u"&Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnAceptar.SetDefault() 
		bSizer6.Add( self.btnAceptar, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnCerrar = wx.Button( self, wx.ID_ANY, u"&Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btnCerrar, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtBusqueda.Bind( wx.EVT_CHAR, self.txtBusquedaOnChar )
		self.btnAceptar.Bind( wx.EVT_BUTTON, self.btnAceptarOnButtonClick )
		self.Bind(wx.EVT_BUTTON, self.btnCerrarOnButtonClick, self.btnCerrar)
		
		self.grdDatos.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnCellChange)
		self.__relaciones__ = relaciones.Relaciones()


	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def txtBusquedaOnChar( self, event ):
		keycode = event.GetKeyCode()
		self.ArmaGrilla()
		event.Skip()
	
	def btnAceptarOnButtonClick( self, event ):
		self.Close(True) 
		self.MakeModal(False)
		self.Destroy()
		return self.ValorRetorno
	
	def btnCerrarOnButtonClick(self, event):
		self.MakeModal(False)
		self.Close(True)

	def ArmaGrilla(self):
		numFilas = self.grdDatos.GetNumberRows()
		numCol = self.grdDatos.GetNumberCols()
		
		campo = ""
		for c in self.campos:
			campo += c + ","
		
		campo = campo[:-1]
		
		query = "select " + campo + " from " + self.tabla + \
			" where " + self.CampoBusqueda + " like '%" + self.txtBusqueda.GetValue().upper() + "%'" +\
			" order by " + self.CampoBusqueda + " limit 20"
		data = self.__relaciones__.ConsultaTodo(query)
		
		grid = self.grdDatos
		grid.ClearGrid()
		
		actual, nuevo = (numFilas, len(data))
		if nuevo < actual:
			#- Borro filas:
			grid.DeleteRows(0, actual - nuevo, True)

		if nuevo > actual:
			#- agrego filas:
			grid.AppendRows(nuevo - actual)
		
		actualcol, nuevacol = (numCol, len(self.campos))
		if nuevacol < actualcol:
			grid.DeleteCols(0, nuevacol - actualco, True)
			
		if nuevacol > actualcol:
			grid.AppendCols(nuevacol - actualcol)
			
		i = 0
		for c in self.campos:
			grid.SetColLabelValue(i, c)
			i += 1
			
		for i in range(0,len(data)):
			for j in range(len(self.campos)):
				grid.SetCellValue(i,j,"%s" % data[i][j])
				
		grid.AutoSizeColumns()

	def OnCellChange(self, event):
		self.ValorRetorno = self.grdDatos.GetCellValue(event.GetRow(), 0)
		event.Skip()
	
	def __str__(self):
		return self.ValorRetorno
