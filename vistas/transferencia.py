# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Ppal
###########################################################################

class Ppal ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1035,449 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu3 = wx.Menu()
		self.mnSalir = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"&Salir", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.mnSalir )
		
		self.m_menubar2.Append( self.m_menu3, u"&Archivo" )
		
		self.SetMenuBar( self.m_menubar2 )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblArchivo = wx.StaticText( self, wx.ID_ANY, u"Archivo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblArchivo.Wrap( -1 )
		bSizer1.Add( self.lblArchivo, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20 )
		
		self.gTotal = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gTotal.SetValue( 0 )
		bSizer1.Add( self.gTotal, 1, wx.ALL|wx.EXPAND, 20 )
		
		self.lblReg = wx.StaticText( self, wx.ID_ANY, u"Registro", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblReg.Wrap( -1 )
		bSizer1.Add( self.lblReg, 1, wx.ALL|wx.EXPAND, 20 )
		
		self.gTabla = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.gTabla.SetValue( 0 )
		bSizer1.Add( self.gTabla, 1, wx.ALL|wx.EXPAND, 20 )
		
		self.btnIniciar = wx.Button( self, wx.ID_ANY, u"&Iniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnIniciar, 1, wx.ALL|wx.EXPAND, 20 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.mnSalirOnMenuSelection, id = self.mnSalir.GetId() )
		self.btnIniciar.Bind( wx.EVT_BUTTON, self.btnIniciarOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def mnSalirOnMenuSelection( self, event ):
		event.Skip()
	
	def btnIniciarOnButtonClick( self, event ):
		event.Skip()
	

