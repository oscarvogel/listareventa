#! /usr/bin/python
#encoding:utf-8
# ...
# ModuleFinder can't handle runtime changes to __path__, but win32com uses them
try:
    # py2exe 0.6.4 introduced a replacement modulefinder.
    # This means we have to add package paths there, not to the built-in
    # one.  If this new modulefinder gets integrated into Python, then
    # we might be able to revert this some day.
    # if this doesn't work, try import modulefinder
    try:
        import py2exe.mf as modulefinder
    except ImportError:
        import modulefinder
    import win32com, sys
    for p in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", p)
    for extra in ["win32com.shell"]: #,"win32com.mapi"
        __import__(extra)
        m = sys.modules[extra]
        for p in m.__path__[1:]:
            modulefinder.AddPackagePath(extra, p)
except ImportError:
    # no build path setup, no worries.
    pass
	
from distutils.core import setup
import py2exe
# -*- coding: utf-8 -*-

import sys
from distutils.core import setup

kwargs = {}

if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'listareventa.pyw',
            'description'    : 'Sistema de revendedores para la consulta de precios y varios.',
            'icon_resources' : [(0, 'graphics\logo.ico')],
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='Ferreteria Avenida SA',
    author='Ferreteria Avenida SA',
    author_email='avenida@ferreteriaavenida.com.ar',
    license="Todos los derechos reservados a Ferreteria Avenida SA (c)",
    **kwargs)