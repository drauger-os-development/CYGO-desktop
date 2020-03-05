#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  cygo-desktop.py
#
#  Copyright 2020 Thomas Castleman <contact@draugeros.org>
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
import webview
# from sys import argv

# try:
	# if argv[1] == "FIRST-TIME-URL":
		# URL = "https://desktop.cygonetwork.com/draugeros-firstrun/"
	# else:
		# URL = "https://u.cygonetwork.com/sign-in"
# except:
	# URL = "https://u.cygonetwork.com/sign-in"

URL = "https://u.cygonetwork.com/sign-in"

web = webview.create_window("CYGO Desktop", URL)
webview.start()
