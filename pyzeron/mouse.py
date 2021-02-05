# Importing extensions and packages
import pygame as _pygame

# Initializing pygame
_pygame.init()

# Functions
# Getting if the mouse is pressed
def get_pressed(button):
	mouse = _pygame.mouse.get_pressed()

	if button == "left":
		return mouse[0]
	elif button == "middle":
		return mouse[1]
	elif button == "right":
		return mouse[2]
	else:
		raise TypeError("get_pressed() unknown button: '"+button+"'")

# Getting the mouse position
def get_position():
	mouse = _pygame.mouse.get_pos()
	return mouse

# Setting the mouse position
def set_position(x, y):
	return _pygame.mouse.set_pos((x, y))
