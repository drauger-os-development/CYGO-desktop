#!/bin/bash
# -*- coding: utf-8 -*-
#
#  detect-installed-games.sh
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
cd  /usr/share/applications
APT_INSTALLED=$(grep --files-with-matches 'Game' $(ls))
list=""
for each in $APT_INSTALLED; do
	add=$(grep "Name=" "$each" | head -1 | sed "s/Name=//")
	if [ "$list" == "" ]; then
		list="$add"
	else
		list="$list
$add"
	fi
done
APT_INSTALLED="$list"
if $(echo "$APT_INSTALLED" | grep -q "Steam"); then
	APT_INSTALLED=$(echo "$APT_INSTALLED" | sed "s/Steam//")
	STEAM_INSTALLED=$(ls $HOME/.local/share/Steam/steamapps/common | sed "/^Proton/ d")
	STEAM_INSTALLED=$(echo "$STEAM_INSTALLED" | sed "s/Steam.dll\|Steamworks Shared//g")
	STEAM_INSTALLED=$(echo "$STEAM_INSTALLED" | sed "s/nmrih/No More Room in Hell/g")
	STEAM_INSTALLED=$(echo "$STEAM_INSTALLED" | sed "s/TheDishwasherVampireSmile/The Dishwasher: Vampire Smile/g")
fi
echo "$APT_INSTALLED"
echo "--------------------------------------------------------------"
echo "$STEAM_INSTALLED"

