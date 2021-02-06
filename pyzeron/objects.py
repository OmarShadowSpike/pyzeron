# Importing extensions and packages
import pygame as _pygame
from pygame.math import Vector2 as _Vector2
from . import mouse as _mouse

# Initializing pygame
_pygame.init()

# Classes
# Sprite class
class Sprite():
	def __init__(self, x, y, image):
		self.x = x
		self.y = y
		self.image = image
		self.rect = self.image.get_rect()
		self.visible = True

	def set_image(self, image):
		self.image = image

	def move(self, x, y):
		self.x += x
		self.y += y

# Rect class
class Rect(_pygame.Rect):
	def __init__(self, x, y, width, height, color=(255, 255, 255)):
		super(Rect, self).__init__(x, y, width, height)

		self.color = (255, 255, 255)
		self.visible = True
		self.rect = self

	def set_color(self, color):
		self.color = color

	def move(self, x, y):
		self.x += x
		self.y += y

# Circle class
class Circle(_pygame.Rect):
	def __init__(self, x, y, width, height, color=(255, 255, 255)):
		super(Circle, self).__init__(x, y, width, height)

		self.color = (255, 255, 255)
		self.visible = True
		self.rect = self

	def set_color(self, color):
		self.color = color

	def move(self, x, y):
		self.x += x
		self.y += y

# Button class
class Button():
	def __init__(self, x, y, width, height, color, event=None):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = color
		self.hover_color = (color[0]+20, color[1]+20, color[2]+20)
		self.event = event
		self.visible = True

	def set_color(self, color):
		self.color = color

	def set_hover_color(self, color):
		self.hover_color = color

	def set_event(self, evt):
		self.event = evt

	def _get_draw(self):
		if self.x+self.width > _mouse.get_position()[0] > self.x and self.y+self.height > _mouse.get_position()[1] > self.y:
			if _mouse.get_pressed("left"):
				if self.event != None:
					self.event()
					return False
			return True

# Font class
class Font():
	def __init__(self, font, font_size):
		self.font = font
		self.font_size = font_size
		self.font_main = _pygame.font.Font(font, font_size)

# Label class
class Label():
	def __init__(self, font, title, color, x, y, center=True):
		self.font = font
		self.title = title
		self.color = color
		self.center = center
		self.visible = True
		self.x = x
		self.y = y
		self.label = self.font.font_main.render(self.title, False, self.color)

# Line class
class Line():
	def __init__(self, pos1, pos2, color=(255, 255, 255)):
		self.pos1 = _Vector2(pos1[0], pos1[1])
		self.pos2 = _Vector2(pos2[0], pos2[1])
		self.color = color
		self.visible = True

	def move_pos1(self, x, y):
		self.pos1.x += x
		self.pos1.y += y

	def move_pos2(self, x, y):
		self.pos2.x += x
		self.pos2.y += y

	def set_pos1(self, pos):
		self.pos1 = _Vector2(pos[0], pos[1])

	def set_pos2(self, pos):
		self.pos2 = _Vector2(pos[0], pos[1])

	def set_color(self, color):
		self.color = color
