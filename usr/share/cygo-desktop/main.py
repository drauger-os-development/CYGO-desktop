#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cygo-desktop.py
#
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
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

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import webkit
import gobject

class webview(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="CYGO Desktop)
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)
		
		self.bro = webkit.WebView()
		self.bro.open("https://cygo.network")
		self.grid.attach(self.bro, 1, 1, 1, 1)

def show_webview():
	window = webview()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main()
	window.connect("delete-event", Gtk.main_quit)
 
 show_webview()
