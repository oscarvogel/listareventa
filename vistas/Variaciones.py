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
from datetime import date
from sistema import funciones, globalDef

###########################################################################
## Class Variaciones
###########################################################################

class Variaciones ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 794,506 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Variaciones de precios", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.m_staticText2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_staticText2.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer2.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Fecha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 1, wx.ALL, 5 )
		
		self.FechaVariacion = wx.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT )
		bSizer3.Add( self.FechaVariacion, 1, wx.ALL, 5 )
		
		cboIVAChoices = [ u"Con IVA", u"Sin IVA" ]
		self.cboIVA = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cboIVAChoices, 0 )
		self.cboIVA.SetSelection( 0 )
		bSizer3.Add( self.cboIVA, 1, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 0, 0, 5 )
		
		self.grdDatos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDatos.CreateGrid( 0, 0 )
		self.grdDatos.EnableEditing( True )
		self.grdDatos.EnableGridLines( True )
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
		bSizer2.Add( self.grdDatos, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnExcel = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/excel2007_d.JPG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnExcel.SetBitmapFocus( wx.Bitmap( u"graphics/excel2007_d.JPG", wx.BITMAP_TYPE_ANY ) )
		self.btnExcel.SetBitmapHover( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		bSizer4.Add( self.btnExcel, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnImprimir = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/printer-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnImprimir.SetBitmapSelected( wx.Bitmap( u"graphics/printer.png", wx.BITMAP_TYPE_ANY ) )
		self.btnImprimir.SetBitmapFocus( wx.Bitmap( u"graphics/printer.png", wx.BITMAP_TYPE_ANY ) )
		self.btnImprimir.SetBitmapHover( wx.Bitmap( u"graphics/printer.png", wx.BITMAP_TYPE_ANY ) )
		self.btnImprimir.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer4.Add( self.btnImprimir, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCerrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/LogOut-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnCerrar.SetBitmapSelected( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnCerrar.SetBitmapHover( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		bSizer4.Add( self.btnCerrar, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		self.cIVA = self.cboIVA.GetSelection()
		fecha = self.FechaVariacion.GetValue()
		self._fecha = fecha.Format("%Y-%m-%d")
		
		self.data = GridData(self._fecha, self.cIVA)
		self.grdDatos.SetTable(self.data)
		self.grdDatos.Refresh()
		self.grdDatos.AutoSizeColumns()
		
		self.__funciones__ = funciones.Funciones()
		self._bd = relaciones.Relaciones()
		# Connect Events
		self.FechaVariacion.Bind( wx.EVT_DATE_CHANGED, self.FechaVariacionOnDateChanged )
		self.cboIVA.Bind( wx.EVT_CHOICE, self.cboIVAOnChoice )
		self.btnExcel.Bind( wx.EVT_BUTTON, self.btnExcelOnButtonClick )
		self.btnImprimir.Bind( wx.EVT_BUTTON, self.btnImprimirOnButtonClick )
		self.btnCerrar.Bind( wx.EVT_BUTTON, self.btnCerrarOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FechaVariacionOnDateChanged( self, event ):
		fecha = self.FechaVariacion.GetValue()
		self._fecha = fecha.Format("%Y-%m-%d")
		self.data = GridData(self._fecha, self.cIVA)
		
		self.grdDatos.SetTable(self.data)
		self.grdDatos.Refresh()
		self.grdDatos.AutoSizeColumns()
		event.Skip()
	
	def cboIVAOnChoice( self, event ):
		self.cIVA = event.GetSelection()
		self.data = GridData(self._fecha, self.cIVA)
		self.grdDatos.SetTable(self.data)
		self.grdDatos.Refresh()
		self.grdDatos.AutoSizeColumns()
		event.Skip()
	
	def btnExcelOnButtonClick( self, event ):
		self.ExportaExcel()
		event.Skip()
	
	def btnImprimirOnButtonClick( self, event ):
		event.Skip()
	
	def btnCerrarOnButtonClick( self, event ):
		self.Close()

		
	def ExportaExcel(self):
		import xlsxwriter
		
		if globalDef.glb_lista == '1':
			query = "select codigo, unidad, detalle, 100 - precioantl1 / precioactl1 * 100 "\
						" from variacion " \
						" where fechaact = '" + self._fecha + "'" +\
						" order by fechaact"
		else:
			query = "select codigo, unidad, detalle, 100 - precioantl4 / precioactl4 * 100 "\
						" from variacion " \
						" where fechaact = '" + self._fecha + "'" +\
						" order by fechaact"
						
		data = self._bd.ConsultaTodo(query)
		workbook = xlsxwriter.Workbook("variaciones.xlsx")
		
		worksheet = workbook.add_worksheet('Variacion') 
		
		col = 0 
		row = 0
		worksheet.write(row, col, u'Codigo')
		worksheet.write(row, col + 1, u'Unidad')
		worksheet.write(row, col + 2, u'Detalle')
		worksheet.write(row, col + 3, u'Variacion')
		worksheet.set_column(0, 0, 7.50)
		worksheet.set_column(1, 0, 7.50)
		worksheet.set_column(2, 0, 50)
		worksheet.set_column(3, 0, 7)
		
		format_number = workbook.add_format()
		format_number.set_num_format('###,##0.00')
		for codigo, unidad, detalle, variacion in (data):
			worksheet.write(row, col,     codigo)
			worksheet.write(row, col + 1, unidad)
			worksheet.write(row, col + 2, detalle)
			if not variacion is None:
				worksheet.write_number(row, col + 3, variacion, format_number)
			else:
				worksheet.write_number(row, col + 3, 0, format_number)
			row += 1
			 
		workbook.close()
		self.__funciones__.Info(message = "Datos exportados a Excel", ventana = self)
	
class GridData(wx.grid.PyGridTableBase):
	
	def __init__(self, fecha = None, cIVA = 0):
		wx.grid.PyGridTableBase.__init__(self)
		
		self._bd = relaciones.Relaciones()
		self._cols = ["Codigo", "Unidad", "Detalle", "Fecha Act", "Prec. Ant.", "Prec. Act.", "Variacion"]
		
		self._fecha = fecha
		
		info = self._bd.ConsultaUno("select * from info")
		
		if info[0][-1] == '1':
			if cIVA == 0:
				query = "select v.codigo, v.unidad, v.detalle, v.fechaact, "\
						" v.precioantl1 + v.precioantl1 * l.iva / 100 precioantl1, "\
						" v.precioactl1 + v.precioactl1 * l.iva / 100 precioactl1, "\
						" 100 - v.precioantl1 / v.precioactl1 * 100 "\
						" from variacion v " \
						" inner join lista l on v.codigo = l.codigo " \
						" where v.fechaact = '" + self._fecha + "'" +\
						" order by v.fechaact"
			else:
				query = "select codigo, unidad, detalle, fechaact, precioantl1, precioactl1, 100 - precioantl1 / precioactl1 * 100 "\
						" from variacion " \
						" where fechaact = '" + self._fecha + "'" +\
						" order by fechaact"
		else:
			if cIVA == 0:
				query = "select v.codigo, v.unidad, v.detalle, v.fechaact, "\
						" v.precioantl4 + v.precioantl4 * l.iva / 100, "\
						" v.precioactl4 + v.precioantl4 * l.iva / 100, "\
						" 100 - v.precioantl4 / v.precioactl4 * 100 "\
						" from variacion v " \
						" inner join lista l on v.codigo = l.codigo " \
						" where v.fechaact = '" + self._fecha + "'" +\
						" order by v.fechaact"
			else:
				query = "select codigo, unidad, detalle, fechaact, precioantl4, precioactl4, 100 - precioantl4 / precioactl4 * 100 "\
						" from variacion " \
						" where fechaact = '" + self._fecha + "'" +\
						" order by fechaact"
			
		self._data = self._bd.ConsultaTodo(query)
		self._highlighted = set()
		
	def GetColLabelValue(self, col):
		return self._cols[col]

	def GetNumberRows(self):
		return len(self._data)

	def GetNumberCols(self):
		return len(self._cols)

	def GetValue(self, row, col):
		return self._data[row][col]

	def SetValue(self, row, col, val):
		self._data[row][col] = val

	def GetAttr(self, row, col, kind):
		attr = wx.grid.GridCellAttr()
		attr.SetBackgroundColour(wx.GREEN if row in self._highlighted else wx.WHITE)
		return attr

	def set_value(self, row, col, val):
		self._highlighted.add(row)
		self.SetValue(row, col, val)

	
