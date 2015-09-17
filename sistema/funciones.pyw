#!/usr/bin/env python
# -*- coding: utf-8 -*-

from win32api import GetFileVersionInfo, LOWORD, HIWORD
from urllib import urlretrieve, urlcleanup
from _winreg import *
from win32com.client import Dispatch
import os.path
from datetime import date
import wx
from vistas import Busqueda


class Funciones():

	def get_version_number (self, filename):
		try:
			info = GetFileVersionInfo (filename, "\\")
			ms = info['FileVersionMS']
			ls = info['FileVersionLS']
			return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
		except:
			return 0,0,0,0

	def status(self, count, data_size, total_data):
		"""Llamado por cada bloque de datos recibido"""
		print count, data_size, total_data

	def descarga(self, url, callback = None):
		#url = ("http://www.ferreteriaavenida.com.ar/serverupdate/farmacia.exe.zip.zip")

		# Nombre del archivo a partir del URL
		filename = url[url.rfind("/") + 1:]

		while not filename:
			filename = raw_input("No se ha podido obtener el nombre del "
								 "archivo.\nEspecifique uno: ")

		print "Descargando %s..." % filename
		
		try:
			if callback is None:
				urlretrieve(url, filename)  # Descargar archivo
			else:
				urlretrieve(url, filename, callback)  # Descargar archivo
			urlcleanup()  #  Limpiar cache
			print "%s descargado correctamente." % filename
		except:
			self.Info("Se ha producido un error en la descarga del archivo. Vuelva a intentarlo mas tarde")
		
	def createShortcut(self, archivo, target='', wDir=None, icon=''):
		print archivo 
		if wDir is None :
			wDir = os.path.dirname(os.path.abspath(target))
		
		ext = archivo[-3:]
		if ext == 'url':
			shortcut = file(archivo, 'w')
			shortcut.write('[InternetShortcut]\n')
			shortcut.write('URL=%s' % target)
			shortcut.close()
		else:
			shell = Dispatch('WScript.Shell')
			shortcut = shell.CreateShortCut(archivo)
			shortcut.Targetpath = target
			shortcut.WorkingDirectory = wDir
			if icon <> '':
				shortcut.IconLocation = icon
			shortcut.save()
			
	def Warn(self, message, ventana, caption = 'Error'):
		dlg = wx.MessageDialog(ventana, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()
		
	def Info(self, message, ventana, caption = 'Sistema de revendedores'):
		dlg = wx.MessageDialog(ventana, message, caption, wx.OK | wx.ICON_INFORMATION)
		dlg.ShowModal()
		dlg.Destroy()
	

class Selecciona(Busqueda.Ppal):
	
	def Buscar(self, ventana, tabla):
		b = Busqueda.Ppal(ventana)
		b.campos = ["codigo", "nombre"]
		b.tabla = tabla
		b.CampoBusqueda = "nombre"
		b.CenterOnParent(wx.BOTH)
		b.ShowModal()

		return b.ValorRetorno
		

