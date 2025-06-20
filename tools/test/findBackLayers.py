#!/usr/bin/env ../utility/fontforge-interp.sh
from __future__ import print_function
__license__ = """
This file is part of GNU FreeFont.

GNU FreeFont is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

GNU FreeFont is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
GNU FreeFont.  If not, see <http://www.gnu.org/licenses/>. 
"""
__author__ = "Stevan White"
__email__ = "stevan.white@googlemail.com"
__copyright__ = "Copyright 2009, 2010, 2018, 2025 Stevan White"
__date__ = "$Date::                           $"
__version__ = "$Revision$"

__doc__ = """
Check for glyphs with back layers.
"""

import fontforge
from sys import argv, exit
from glob import glob
from os import path

problem = False

def checkBackLayers( fontDir, fontFile ):
	if isinstance( fontFile, ( list, tuple ) ):
		print( "Checking for back layers in directory", fontDir )
		for fontName in fontFile:
			checkBackLayers( fontDir, fontName )
		return

	font = fontforge.open( path.join( fontDir, fontFile ) )
	g = font.selection.all()
	g = font.selection.byGlyphs

	print( "Checking for back layers in file", fontFile )
	for e in g:
		if e.layer_cnt > 0 and e.layers[0]: # 0 is the background layer!
			print( '\t', e.glyphname )

# --------------------------------------------------------------------------
args = argv[1:]

if len( args ) < 1 or len( args[0].strip() ) == 0:
	checkBackLayers( '../../sfd/',
		( 'FreeSerif.sfd', 'FreeSerifItalic.sfd',
		'FreeSerifBold.sfd', 'FreeSerifBoldItalic.sfd',
		'FreeSans.sfd', 'FreeSansOblique.sfd',
		'FreeSansBold.sfd', 'FreeSansBoldOblique.sfd',
		'FreeMono.sfd', 'FreeMonoOblique.sfd',
		'FreeMonoBold.sfd', 'FreeMonoBoldOblique.sfd' ) )
elif len( args ) == 2:
	checkBackLayers( args[0], glob( args[1], root_dir=args[0] ) )
else:
	checkBackLayers( args[0], args[1:] )

if not problem:
	exit( 0 )
else:
	exit( 1 )
