#!/usr/bin/env python

import getpass
import os


selectedOption = 'b'
print "\nHello, %s!" % (getpass.getuser())
while(1):
	if selectedOption == 'b':
		os.system('clear')
		print "Welcome to Nunchuk Mashers!"
		print "To read the instructions, press i."
		print "To start the game, press s."
		selectedOption = raw_input()
	if selectedOption == 'i':
		os.system('clear')
		print "The instructions for Nunchuk Mashers will go here."
		print "Press any key to return to the opening screen."
		if raw_input():
			selectedOption = 'b'
	if selectedOption == 's':
		os.system('clear')
		break
print "The beginning of the game will start here."
