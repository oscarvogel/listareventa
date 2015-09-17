#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  validaciones.py
#  
#  Copyright 2015  <>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import wx


class ValidaCliente(wx.PyValidator):
	def __init__(self):
		""" Standard constructor.
		"""
		wx.PyValidator.__init__(self)
		#self.Bind(wx.EVT_CHAR, self.OnChar)


	def Clone(self):
		""" Standard cloner.
			Note that every validator must implement the Clone() method.
		"""
		return ValidaCliente()

	def TransferToWindow(self):
		""" Transfer data from validator to window.
			The default implementation returns False, indicating that an error
			occurred.  We simply return True, as we don't do any data transfer.
		"""
		return True # Prevent wxDialog from complaining.


	def TransferFromWindow(self):
		""" Transfer data from window to validator.
			The default implementation returns False, indicating that an error
			occurred.  We simply return True, as we don't do any data transfer.
		"""
		return True # Prevent wxDialog from complaining.
		
	def Validate(self, win):
		txtCtrl = self.GetWindow()
		text = txtCtrl.GetValue()
		print text
		return False
	
	def OnChar(self, event):
		key = int(event.GetKeyCode()) 
		print key

