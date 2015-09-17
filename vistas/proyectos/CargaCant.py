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

class Ppal ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 504,224 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		SizerPpal = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitulo = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblTitulo.Wrap( -1 )
		self.lblTitulo.SetFont( wx.Font( 16, 70, 90, 90, False, "@Arial Unicode MS" ) )
		self.lblTitulo.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.lblTitulo.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		SizerPpal.Add( self.lblTitulo, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gCantSizer = wx.GridSizer( 0, 3, 0, 0 )
		
		self.lblCantidad = wx.StaticText( self, wx.ID_ANY, u"Cantidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCantidad.Wrap( -1 )
		gCantSizer.Add( self.lblCantidad, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtCantidad = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gCantSizer.Add( self.txtCantidad, 0, wx.ALL, 5 )
		
		self.lblUnidad = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblUnidad.Wrap( -1 )
		self.lblUnidad.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gCantSizer.Add( self.lblUnidad, 0, wx.ALL, 5 )
		
		
		SizerPpal.Add( gCantSizer, 1, wx.EXPAND, 5 )
		
		gCajasSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lblCajas = wx.StaticText( self, wx.ID_ANY, u"Cajas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCajas.Wrap( -1 )
		gCajasSizer.Add( self.lblCajas, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtCajas = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_READONLY )
		gCajasSizer.Add( self.txtCajas, 0, wx.ALL, 5 )
		
		
		SizerPpal.Add( gCajasSizer, 1, wx.EXPAND, 5 )
		
		gDescSizer = wx.GridSizer( 0, 2, 0, 0 )
		
		self.lblDescripcion = wx.StaticText( self, wx.ID_ANY, u"Descripcion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblDescripcion.Wrap( -1 )
		gDescSizer.Add( self.lblDescripcion, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtDescripcion = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_READONLY )
		gDescSizer.Add( self.txtDescripcion, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		SizerPpal.Add( gDescSizer, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAceptar = wx.Button( self, wx.ID_ANY, u"&Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnAceptar, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnCerrar = wx.Button( self, wx.ID_ANY, u"&Cerrar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnCerrar, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		SizerPpal.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( SizerPpal )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.PpalOnInitDialog )
		self.Bind( wx.EVT_SET_FOCUS, self.PpalOnSetFocus )
		self.txtCantidad.Bind( wx.EVT_CHAR, self.txtCantidadOnChar )
		self.txtCantidad.Bind( wx.EVT_KEY_UP, self.txtCantidadOnKeyUp )
		self.txtCantidad.Bind( wx.EVT_KILL_FOCUS, self.txtCantidadOnKillFocus )
		self.txtCajas.Bind( wx.EVT_CHAR, self.txtCajasOnChar )
		self.txtCajas.Bind( wx.EVT_KILL_FOCUS, self.txtCajasOnKillFocus )
		self.btnAceptar.Bind( wx.EVT_BUTTON, self.btnAceptarOnButtonClick )
		self.btnCerrar.Bind( wx.EVT_BUTTON, self.btnCerrarOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def PpalOnInitDialog( self, event ):
		event.Skip()
	
	def PpalOnSetFocus( self, event ):
		event.Skip()
	
	def txtCantidadOnChar( self, event ):
		event.Skip()
	
	def txtCantidadOnKeyUp( self, event ):
		event.Skip()
	
	def txtCantidadOnKillFocus( self, event ):
		event.Skip()
	
	def txtCajasOnChar( self, event ):
		event.Skip()
	
	def txtCajasOnKillFocus( self, event ):
		event.Skip()
	
	def btnAceptarOnButtonClick( self, event ):
		event.Skip()
	
	def btnCerrarOnButtonClick( self, event ):
		event.Skip()
	

