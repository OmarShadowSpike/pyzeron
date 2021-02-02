# Importing extensions and packages
import pygame as _pygame
import sys
import random

# Initializing pygame
_pygame.init()

# Functions
# Loading an image
def loadImage(file):
	return _pygame.image.load(file)

# Loading a sound
def loadSound(file):
	return _pygame.mixer.Sound(file)

# Loading the music
def loadMusic(file):
	return _pygame.mixer.music.load(file)

# Playing the music
def playMusic():
	return _pygame.mixer.music.play(-1)

# Checking if objects are colliding
def collideCheck(obj1, obj2):
	if obj1 == Sprite:
		return obj1.rect.colliderect(obj2)
	elif obj2 == Sprite:
		return obj1.colliderect(obj2.rect)
	elif obj1 == Spirte and obj2 == Sprite:
		return obj1.rect.colliderect(obj2.rect)

	return obj1.colliderect(obj2)
