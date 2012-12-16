from pygame import *

#	Font Pallet
# Strings with personalized fonts
# For PyGame

class fontPallet(object):
	# Initializes the object
	# The size must be a square size containing each letter
	def __init__(self, size, palletImage):
		super(fontPallet, self).__init__()
		self.fontSurface = image.load(palletImage)
		self.size = size
		self.charactersize = (size, size) # Always a square

	# Prints a text to the given display
	def printf(self, display,string="", pos=(0, 0)):
		strlen = len(string)
		printSurface = Surface((strlen*self.size, self.size))
		for index in range(strlen):
			self.fontTable(printSurface, string[index], index)
		display.blit(printSurface,pos)
	# Usage: 
	# 	- myText = fontPallet(size)
	#		- myText.printf(mainDisplay, "some text", (x_coordinate, y_coordinate))

	# A table for assign each letter to a position
	# Currently supports only ENG alphabets, numbers, ! and ?
	def fontTable(self, printSurface, letter, index):
		# Default positions
		x = y = 0
		# Conditions for each letter
		# (I didn't enjoyed doing this)
		if letter == 'A':
			pass
		if letter == 'B':
			x = 1
		if letter == 'C':
			x = 2
		if letter == 'D':
			x = 3
		if letter == 'E':
			x = 4
		if letter == 'F':
			x = 5
		if letter == 'G':
			x = 6
		if letter == 'H':
			x = 7
		if letter == 'I':
			x = 8
		if letter == 'J':
			x = 9
		if letter == 'K':
			x = 10
		if letter == 'L':
			x = 11
		if letter == 'M':
			x = 12
		if letter == 'N':
			x = 13
		if letter == 'O':
			x = 14
		if letter == 'P':
			x = 15
		if letter == 'Q':
			x = 0
			y = 1
		if letter == 'R':
			x = 1
			y = 1
		if letter == 'S':
			x = 2
			y = 1
		if letter == 'T':
			x = 3
			y = 1
		if letter == 'U':
			x = 4
			y = 1
		if letter == 'V':
			x = 5
			y = 1
		if letter == 'W':
			x = 6
			y = 1
		if letter == 'X':
			x = 7
			y = 1
		if letter == 'Y':
			x = 8
			y = 1
		if letter == 'Z':
			x = 9
			y = 1

		# This is so crappy
		if letter == 'a':
			x = 10
			y = 1
		if letter == 'b':
			x = 11
			y = 1
		if letter == 'c':
			x = 12
			y = 1
		if letter == 'd':
			x = 13
			y = 1
		if letter == 'e':
			x = 14
			y = 1
		if letter == 'f':
			x = 15
			y = 1
		if letter == 'g':
			x = 0
			y = 2
		if letter == 'h':
			x = 1
			y = 2
		if letter == 'i':
			x = 2
			y = 2
		if letter == 'j':
			x = 3
			y = 2
		if letter == 'k':
			x = 4
			y = 2
		if letter == 'l':
			x = 5
			y = 2
		if letter == 'm':
			x = 6
			y = 2
		if letter == 'n':
			x = 7
			y = 2
		if letter == 'o':
			x = 8
			y = 2
		if letter == 'p':
			x = 9
			y = 2
		if letter == 'q':
			x = 10
			y = 2
		if letter == 'r':
			x = 11
			y = 2
		if letter == 's':
			x = 12
			y = 2
		if letter == 't':
			x = 13
			y = 2
		if letter == 'u':
			x = 14
			y = 2
		if letter == 'v':
			x = 15
			y = 2
		if letter == 'w':
			x = 0
			y = 3
		if letter == 'x':
			x = 1
			y = 3
		if letter == 'y':
			x = 2
			y = 3
		if letter == 'z':
			x = 3
			y = 3
		if letter == '0':
			x = 4
			y = 3
		if letter == '1':
			x = 5
			y = 3
		if letter == '2':
			x = 6
			y = 3
		if letter == '3':
			x = 7
			y = 3
		if letter == '4':
			x = 8
			y = 3
		if letter == '5':
			x = 9
			y = 3
		if letter == '6':
			x = 10
			y = 3
		if letter == '7':
			x = 11
			y = 3
		if letter == '8':
			x = 12
			y = 3
		if letter == '9':
			x = 13
			y = 3
		if letter == '!':
			x = 14
			y = 3
		if letter == '?':
			x = 15
			y = 3
		if letter == ' ':
			x = 0
			y = 4
		if letter == '.':
			x = 1
			y = 4
		if letter == ':':
			x = 2
			y = 4
		if letter == ',':
			x = 3
			y = 4
		if letter == '-':
			x = 4
			y = 4
		# It's ugly, but necessary
		# Now, creates a rectangular area os size*size
		# Print on a surface that later, will be printed on main display
		area = Rect((x*self.size, y*self.size),(self.size, self.size))
		printSurface.blit(self.fontSurface,(index*self.size, 0),area)

######################### END #########################################