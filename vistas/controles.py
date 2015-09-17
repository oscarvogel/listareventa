# -*- coding: utf-8 -*- 

import wx
import wx.combo 

class Controles:
	
	def CreaCombo(panel, log=None, style=0):
		# Create a ComboCtrl
		cc = wx.ComboBox(panel, style=style, size=(250,-1))
		
		# Create a Popup
		popup = ListCtrlComboPopup(log)
		
		# Associate them with each other.  This also triggers the
		# creation of the ListCtrl.
		cc.SetPopupControl(popup)

		# Add some items to the listctrl.
		for x in range(75):
			popup.AddItem("Item-%02d" % x)

		return cc