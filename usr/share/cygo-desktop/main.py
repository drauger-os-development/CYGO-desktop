#!/usr/bin/env python3
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
import webview
import threading
from time import sleep
from sys import argv

if sys.argv[1] == "FIRST-TIME-URL":
	URL="https://desktop.cygonetwork.com/draugeros-firstrun/"
else
	URL="https://u.cygonetwork.com/sign-in"

def load_html():
    webview.load_html("""
    <style>
        body {
            background-color: #333;
            color: white;
            font-family: Helvetica Neue, Helvetica, Arial, sans-serif;
        }

        .main-container {
            width: 100%;
            height: 90vh;
            display: flex;
            display: -webkit-flex;
            align-items: center;
            -webkit-align-items: center;
            justify-content: center;
            -webkit-justify-content: center;
            overflow: hidden;
        }

        .loading-container {
        }

        .loader {
          font-size: 10px;
          margin: 50px auto;
          text-indent: -9999em;
          width: 3rem;
          height: 3rem;
          border-radius: 50%;
          background: #ffffff;
          background: -moz-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
          background: -webkit-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
          background: -o-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
          background: -ms-linear-gradient(left, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
          background: linear-gradient(to right, #ffffff 10%, rgba(255, 255, 255, 0) 42%);
          position: relative;
          -webkit-animation: load3 1.4s infinite linear;
          animation: load3 1.4s infinite linear;
          -webkit-transform: translateZ(0);
          -ms-transform: translateZ(0);
          transform: translateZ(0);
        }
        .loader:before {
          width: 50%;
          height: 50%;
          background: #ffffff;
          border-radius: 100% 0 0 0;
          position: absolute;
          top: 0;
          left: 0;
          content: '';
        }
        .loader:after {
          background: #333;
          width: 75%;
          height: 75%;
          border-radius: 50%;
          content: '';
          margin: auto;
          position: absolute;
          top: 0;
          left: 0;
          bottom: 0;
          right: 0;
        }
        @-webkit-keyframes load3 {
          0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
          }
          100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
          }
        }
        @keyframes load3 {
          0% {
            -webkit-transform: rotate(0deg);
            transform: rotate(0deg);
          }
          100% {
            -webkit-transform: rotate(360deg);
            transform: rotate(360deg);
          }
        }

        .loaded-container {
            display: none;
        }


    </style>
    <body>
      <div class="main-container">
          <div id="loader" class="loading-container">
              <div class="loader">Loading...</div>
          </div>

          <div id="main" class="loaded-container">
              <h1>Content is loaded!</h1>
          </div>
      </div>

      <script>
          setTimeout(function() {
              document.getElementById('loader').style.display = 'none'
              document.getElementById('main').style.display = 'block'
          }, 5000)
      </script>
    </body>

    """)

def change_url():
	sleep(3)
	webview.load_url(URL)

if __name__ == '__main__':
    a = threading.Thread(target=load_html)
    a.start()
    b = threading.Thread(target=change_url)
    b.start()

web = webview.create_window("CYGO Desktop", URL, confirm_quit=True, )
