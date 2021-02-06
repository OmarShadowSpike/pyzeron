# Importing extensions and packages
import pygame as _pygame
import keyboard as _keyboard

# Initializing pygame
_pygame.init()

# Checking if a key is pressed
def get_pressed(key):
	return _keyboard.is_pressed(key)
