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
## Class Lista
###########################################################################

class Lista ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 883,558 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.grdDatos = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.grdDatos.CreateGrid( 20, 4 )
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
		bSizer5.Add( self.grdDatos, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnExcel = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/excel2007_d.JPG", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnExcel.SetBitmapSelected( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		self.btnExcel.SetBitmapFocus( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		self.btnExcel.SetBitmapHover( wx.Bitmap( u"graphics/excel2007.jpeg", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.btnExcel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnAgregar = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/document-new-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnAgregar.SetBitmapDisabled( wx.Bitmap( u"graphics/document-new-b.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetBitmapSelected( wx.Bitmap( u"graphics/document-new.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetBitmapFocus( wx.Bitmap( u"graphics/document-new.png", wx.BITMAP_TYPE_ANY ) )
		self.btnAgregar.SetBitmapHover( wx.Bitmap( u"graphics/document-new.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.btnAgregar, 1, wx.ALL, 5 )
		
		self.btnSalir = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/LogOut-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnSalir.SetBitmapSelected( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapFocus( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapHover( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.btnSalir, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtBusqueda.Bind( wx.EVT_CHAR, self.txtBusquedaOnChar )
		self.cboEntrega.Bind( wx.EVT_CHOICE, self.cboEntregaOnChoice )
		self.cboIVA.Bind( wx.EVT_CHOICE, self.cboIVAOnChoice )
		self.btnOrdenAlf.Bind( wx.EVT_BUTTON, self.btnOrdenAlfOnButtonClick )
		self.btnOrdenNum.Bind( wx.EVT_BUTTON, self.btnOrdenNumOnButtonClick )
		self.btnExcel.Bind( wx.EVT_BUTTON, self.btnExcelOnButtonClick )
		self.btnAgregar.Bind( wx.EVT_BUTTON, self.btnAgregarOnButtonClick )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.btnSalirOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtBusquedaOnChar( self, event ):
		event.Skip()
	
	def cboEntregaOnChoice( self, event ):
		event.Skip()
	
	def cboIVAOnChoice( self, event ):
		event.Skip()
	
	def btnOrdenAlfOnButtonClick( self, event ):
		event.Skip()
	
	def btnOrdenNumOnButtonClick( self, event ):
		event.Skip()
	
	def btnExcelOnButtonClick( self, event ):
		event.Skip()
	
	def btnAgregarOnButtonClick( self, event ):
		event.Skip()
	
	def btnSalirOnButtonClick( self, event ):
		event.Skip()
	

