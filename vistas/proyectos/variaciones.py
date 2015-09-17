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
		
		self.btnImprimir = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/IMPRIMIR_D.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnImprimir.SetBitmapSelected( wx.Bitmap( u"graphics/IMPRIMIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnImprimir.SetBitmapFocus( wx.Bitmap( u"graphics/IMPRIMIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnImprimir.SetBitmapHover( wx.Bitmap( u"graphics/IMPRIMIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnImprimir.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer4.Add( self.btnImprimir, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCerrar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/SALIR_D.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnCerrar.SetBitmapSelected( wx.Bitmap( u"graphics/SALIR.bmp", wx.BITMAP_TYPE_ANY ) )
		self.btnCerrar.SetBitmapHover( wx.Bitmap( u"graphics/SALIR.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer4.Add( self.btnCerrar, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
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
		event.Skip()
	
	def cboIVAOnChoice( self, event ):
		event.Skip()
	
	def btnExcelOnButtonClick( self, event ):
		event.Skip()
	
	def btnImprimirOnButtonClick( self, event ):
		event.Skip()
	
	def btnCerrarOnButtonClick( self, event ):
		event.Skip()
	

