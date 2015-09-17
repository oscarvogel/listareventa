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
## Class Ppal
###########################################################################

class Ppal ( wx.Frame ):
	
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
		self.grdDet.CreateGrid( 0, 5 )
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
		self.grdDet.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.grdDetOnGridSelectCell )
		self.grdDet.Bind( wx.EVT_KEY_DOWN, self.grdDetOnKeyDown )
		self.btnGraba.Bind( wx.EVT_BUTTON, self.btnGrabaOnButtonClick )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.btnSalirOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def grdArtOnGridSelectCell( self, event ):
		event.Skip()
	
	def grdArtOnKeyDown( self, event ):
		event.Skip()
	
	def grdDetOnGridSelectCell( self, event ):
		event.Skip()
	
	def grdDetOnKeyDown( self, event ):
		event.Skip()
	
	def btnGrabaOnButtonClick( self, event ):
		event.Skip()
	
	def btnSalirOnButtonClick( self, event ):
		event.Skip()
	

