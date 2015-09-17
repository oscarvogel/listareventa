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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ferreteria Avenida SA", pos = wx.DefaultPosition, size = wx.Size( 971,611 ), style = wx.DEFAULT_FRAME_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.lblTitulo = wx.StaticText( self, wx.ID_ANY, u"Ferreteria Avenida SA", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.lblTitulo.Wrap( -1 )
		self.lblTitulo.SetFont( wx.Font( 18, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		self.lblTitulo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.lblTitulo.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer1.Add( self.lblTitulo, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Paginas = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Paginas.SetFont( wx.Font( 12, 74, 90, 92, False, "Arial Black" ) )
		
		self.pagina1 = wx.Panel( self.Paginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 5, 2, 0, 0 )
		
		self.m_staticText2 = wx.StaticText( self.pagina1, wx.ID_ANY, u"Numero de Cliente", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtNroCliente = wx.TextCtrl( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.WANTS_CHARS )
		self.txtNroCliente.SetMaxLength( 8 ) 
		bSizer3.Add( self.txtNroCliente, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lblNombre = wx.StaticText( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombre.Wrap( -1 )
		bSizer3.Add( self.lblNombre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.pagina1, wx.ID_ANY, u"I.V.A.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		optIVAChoices = [ u"0", u"10.5", u"21.00" ]
		self.optIVA = wx.Choice( self.pagina1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, optIVAChoices, 0 )
		self.optIVA.SetSelection( 2 )
		fgSizer1.Add( self.optIVA, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( fgSizer1, 1, wx.ALIGN_RIGHT, 5 )
		
		gSizer2 = wx.GridSizer( 1, 4, 0, 0 )
		
		self.m_staticText5 = wx.StaticText( self.pagina1, wx.ID_ANY, u"D.G.R.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_staticText5, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtDGR = wx.TextCtrl( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gSizer2.Add( self.txtDGR, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.pagina1, wx.ID_ANY, u"Otros. Imp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.m_staticText6, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtOtrosImp = wx.TextCtrl( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gSizer2.Add( self.txtOtrosImp, 0, wx.ALL, 5 )
		
		
		gSizer1.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self.pagina1, wx.ID_ANY, u"Correo Electronico", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer1.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.txtEmail = wx.TextCtrl( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		gSizer1.Add( self.txtEmail, 0, wx.EXPAND, 5 )
		
		self.m_staticText10 = wx.StaticText( self.pagina1, wx.ID_ANY, u"Localidad de Reparto", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		self.m_staticText10.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer1.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txtLocalidad = wx.TextCtrl( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		self.txtLocalidad.SetMaxLength( 4 ) 
		self.txtLocalidad.SetToolTipString( u"Presiona F2 para realizar la busqueda" )

		bSizer4.Add( self.txtLocalidad, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.lblLocalidad = wx.StaticText( self.pagina1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblLocalidad.Wrap( -1 )
		bSizer4.Add( self.lblLocalidad, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self.pagina1, wx.ID_ANY, u"Condicion de Pago", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		cboPagoChoices = []
		self.cboPago = wx.ComboBox( self.pagina1, wx.ID_ANY, u"Condicion de Pago", wx.DefaultPosition, wx.Size( 250,-1 ), cboPagoChoices, wx.TE_PROCESS_ENTER )
		self.cboPago.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )
		
		gSizer1.Add( self.cboPago, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		self.avance = wx.Gauge( self.pagina1, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.avance.SetValue( 0 ) 
		bSizer2.Add( self.avance, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.btnActualizaLista = wx.BitmapButton( self.pagina1, wx.ID_ANY, wx.Bitmap( u"graphics/internet.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnActualizaLista.SetToolTipString( u"Actualizar desde Internet" )
		bSizer2.Add( self.btnActualizaLista, 0, wx.ALL, 5 )
		
		
		self.pagina1.SetSizer( bSizer2 )
		self.pagina1.Layout()
		bSizer2.Fit( self.pagina1 )
		self.Paginas.AddPage( self.pagina1, u"Parametros", True )
		self.pagina2 = wx.Panel( self.Paginas, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 2, 3, 0, 0 )
		
		self.btnListaGeneral = wx.BitmapButton( self.pagina2, wx.ID_ANY, wx.Bitmap( u"graphics/lista.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnListaGeneral.SetToolTipString("Lista general de articulos")
		gSizer3.Add( self.btnListaGeneral, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.btnListaReducida = wx.BitmapButton( self.pagina2, wx.ID_ANY, wx.Bitmap( u"graphics/listareducida.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnListaReducida.SetToolTipString("Lista reducida de articulos")
		gSizer3.Add( self.btnListaReducida, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.btnVentas = wx.BitmapButton( self.pagina2, wx.ID_ANY, wx.Bitmap( u"graphics/ventas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnVentas.SetToolTipString("Ventas de productos")
		gSizer3.Add( self.btnVentas, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.btnVariaciones = wx.BitmapButton( self.pagina2, wx.ID_ANY, wx.Bitmap( u"graphics/variacion.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnVariaciones.SetToolTipString("Variaciones de precios")
		gSizer3.Add( self.btnVariaciones, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnPedidos = wx.BitmapButton( self.pagina2, wx.ID_ANY, wx.Bitmap( u"graphics/pedidos.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.btnVariaciones.SetToolTipString("Pedidos de productos a Ferreteria Avenida SA")
		gSizer3.Add( self.btnPedidos, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.btnOfertas = wx.BitmapButton( self.pagina2, wx.ID_ANY, wx.Bitmap( u"graphics/oferta.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gSizer3.Add( self.btnOfertas, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		self.pagina2.SetSizer( gSizer3 )
		self.pagina2.Layout()
		gSizer3.Fit( self.pagina2 )
		self.Paginas.AddPage( self.pagina2, u"Menu General", False )
		
		bSizer1.Add( self.Paginas, 1, wx.EXPAND |wx.ALL, 5 )
		
		#self.lblMsjSistema = wx.StaticText( self, wx.ID_ANY, u"Mensajes del sistema", wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.lblMsjSistema.Wrap( -1 )
		#bSizer1.Add( self.lblMsjSistema, 0, wx.ALL, 5 )
		
		self.InfoBar = wx.InfoBar( self )
		self.InfoBar.SetShowHideEffects( wx.SHOW_EFFECT_ROLL_TO_BOTTOM, wx.SHOW_EFFECT_ROLL_TO_TOP )
		self.InfoBar.SetEffectDuration( 500 )
		self.InfoBar.SetToolTipString( u"Presiona la X para cerrar" )
		bSizer1.Add( self.InfoBar, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5  )
		
		self.btnSalir = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"graphics/LogOut-b.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.btnSalir.SetBitmapFocus( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		self.btnSalir.SetBitmapHover( wx.Bitmap( u"graphics/LogOut.png", wx.BITMAP_TYPE_ANY ) )
		bSizer1.Add( self.btnSalir, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txtNroCliente.Bind( wx.EVT_CHAR, self.txtNroClienteOnChar )
		self.txtNroCliente.Bind( wx.EVT_KILL_FOCUS, self.txtNroClienteOnKillFocus )
		self.optIVA.Bind( wx.EVT_CHAR, self.optIVAOnChar )
		self.optIVA.Bind( wx.EVT_CHOICE, self.optIVAOnChoice )
		self.txtDGR.Bind( wx.EVT_CHAR, self.txtDGROnChar )
		self.txtDGR.Bind( wx.EVT_KILL_FOCUS, self.txtDGROnKillFocus )
		self.txtOtrosImp.Bind( wx.EVT_CHAR, self.txtOtrosImpOnChar )
		self.txtOtrosImp.Bind( wx.EVT_KILL_FOCUS, self.txtOtrosImpOnKillFocus )
		self.txtEmail.Bind( wx.EVT_KILL_FOCUS, self.txtEmailOnKillFocus )
		self.txtLocalidad.Bind( wx.EVT_CHAR, self.txtLocalidadOnChar )
		self.txtLocalidad.Bind( wx.EVT_KILL_FOCUS, self.txtLocalidadOnKillFocus )
		self.txtLocalidad.Bind( wx.EVT_SET_FOCUS, self.txtLocalidadOnSetFocus )
		self.cboPago.Bind( wx.EVT_CHAR, self.cboPagoOnChar )
		self.cboPago.Bind( wx.EVT_COMBOBOX, self.cboPagoOnCombobox )
		self.btnActualizaLista.Bind( wx.EVT_BUTTON, self.btnActualizaListaOnButtonClick )
		self.btnListaGeneral.Bind( wx.EVT_BUTTON, self.btnListaGeneralOnButtonClick )
		self.btnListaReducida.Bind( wx.EVT_BUTTON, self.btnListaReducidaOnButtonClick )
		self.btnVentas.Bind( wx.EVT_BUTTON, self.btnVentasOnButtonClick )
		self.btnVariaciones.Bind( wx.EVT_BUTTON, self.btnVariacionesOnButtonClick )
		self.btnPedidos.Bind( wx.EVT_BUTTON, self.btnPedidosOnButtonClick )
		self.btnOfertas.Bind( wx.EVT_BUTTON, self.btnOfertasOnButtonClick )
		self.btnSalir.Bind( wx.EVT_BUTTON, self.btnSalirOnButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def txtNroClienteOnChar( self, event ):
		event.Skip()
	
	def txtNroClienteOnKillFocus( self, event ):
		event.Skip()
	
	def optIVAOnChar( self, event ):
		event.Skip()
	
	def optIVAOnChoice( self, event ):
		event.Skip()
	
	def txtDGROnChar( self, event ):
		event.Skip()
	
	def txtDGROnKillFocus( self, event ):
		event.Skip()
	
	def txtOtrosImpOnChar( self, event ):
		event.Skip()
	
	def txtOtrosImpOnKillFocus( self, event ):
		event.Skip()
	
	def txtEmailOnKillFocus( self, event ):
		event.Skip()
	
	def txtLocalidadOnChar( self, event ):
		event.Skip()
	
	def txtLocalidadOnKillFocus( self, event ):
		event.Skip()
	
	def cboPagoOnChar( self, event ):
		event.Skip()
	
	def cboPagoOnCombobox( self, event ):
		event.Skip()
	
	def btnActualizaListaOnButtonClick( self, event ):
		event.Skip()
	
	def btnListaGeneralOnButtonClick( self, event ):
		event.Skip()
	
	def btnListaReducidaOnButtonClick( self, event ):
		event.Skip()
	
	def btnVentasOnButtonClick( self, event ):
		event.Skip()
	
	def btnVariacionesOnButtonClick( self, event ):
		event.Skip()
	
	def btnPedidosOnButtonClick( self, event ):
		event.Skip()
	
	def btnOfertasOnButtonClick( self, event ):
		event.Skip()
	
	def btnSalirOnButtonClick( self, event ):
		event.Skip()
	

