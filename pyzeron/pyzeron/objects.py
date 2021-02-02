# Importing extensions and packages
import pygame
import sys
import random

from pygame.math import Vector2

# Initializing pygame
pygame.init()

# Classes
# Sprite class
class Sprite():
	def __init__(self, x, y, image):
		self.x = x
		self.y = y
		self.rect = pygame.Rect(self.x, self.y, image.get_width(), image.get_height())
		self.border = None
		self.image = image
		self.visible = True

	def setImage(self, image):
		self.image = image

	def setBorder(self, x, y):
		self.border = Vector2(x, y)

	def move(self, x, y):
		self.x += x
		self.y += y

# Rect class
class Rect(pygame.Rect):
	def __init__(self, x, y, width, height, color=(255, 255, 255)):
		super(Rect, self).__init__(x, y, width, height)

		self.color = (255, 255, 255)
		self.border = None
		self.visible = True

	def setColor(self, color):
		self.color = color

	def setBorder(self, x, y):
		self.border = Vector2(x, y)

	def move(self, x, y):
		self.x += x
		self.y += y

# Circle class
class Circle(pygame.Rect):
	def __init__(self, x, y, width, height, color=(255, 255, 255)):
		super(Circle, self).__init__(x, y, width, height)

		self.color = (255, 255, 255)
		self.border = None
		self.visible = True

	def setColor(self, color):
		self.color = color

	def setBorder(self, x, y):
		self.border = Vector2(x, y)

	def move(self, x, y):
		self.x += x
		self.y += y

# Text class
class Text():
	def __init__(self, x, y, title, font=None, fontSize=40, color=(255, 255, 255)):
		self.title = title
		self.pos = self.x, self.y = x, y
		self.font = None
		self.fontSize = fontSize
		self.color = color

	def setColor(self, color):
		self.color = color

	def move(self, x, y):
		self.x += x
		self.y += y
