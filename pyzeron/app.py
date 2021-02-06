# Importing extensions and packages
import pygame as _pygame
import sys as _sys

from .objects import Rect, Circle, Sprite, Label, Line, Button
from .misc import *

# Initializing pygame
_pygame.init()

# App class
class App():
	def __init__(self, title, width, height):
		self.window_size = self.window_width, self.window_height = width, height
		self.window_title = title

		self.sprites = []
		self.rects = []
		self.circles = []
		self.buttons = []
		self.texts = []
		self.lines = []

		self.window_background_color = (20, 20, 20)
		self.window_background_image = None
		self.showing_fps = True
		self.icon = None

		self.fps = 60
		self.current_fps = 60
		self.window = _pygame.display.set_mode(self.window_size)
		_pygame.display.set_caption(self.window_title)

	# Setting the window's background color
	def set_background_color(self, color):
		self.window_background_color = color

	# Setting the window's background image
	def set_background_image(self, image):
		self.window_background_image = image

	# Setting the window's icon
	def set_icon(self, image):
		self.icon = image
		_pygame.display.set_icon(image)

	# Showing the fps
	def show_fps(self):
		self.showing_fps = True

	# Hiding the fps
	def hide_fps(self):
		self.showing_fps = False

	# Drawing sprites in the loop
	def _draw_sprite(self, sprite):
		self.sprites.append(sprite)

	# Drawing rects in the loop
	def _draw_rect(self, rect):
		self.rects.append(rect)

	# Drawing circles in the loop
	def _draw_circle(self, circle):
		self.circles.append(circle)

	# Drawing buttons in the loop
	def _draw_button(self, button):
		self.buttons.append(button)

	# Drawing texts in the loop
	def _draw_text(self, txt):
		self.texts.append(txt)

	# Drawing lines in the loop
	def _draw_line(self, line):
		self.lines.append(line)

	# Drawing objects in the loop
	def draw(self, obj):
		if type(obj) == Sprite:
			self._draw_sprite(obj)
		elif type(obj) == Rect:
			self._draw_rect(obj)
		elif type(obj) == Circle:
			self._draw_circle(obj)
		elif type(obj) == Button:
			self._draw_button(obj)
		elif type(obj) == Label:
			self._draw_text(obj)
		elif type(obj) == Line:
			self._draw_line(obj)

	# Drawing an entire list of objects
	def draw_list(self, list):
		for obj in list:
			self.draw(obj)

	# Running the application
	def run(self, fps=60, loop=None, debug=False):
		self.fps = fps

		print("Starting...")
		print("Stats:")
		print("{")
		print("\tFps:", fps)
		print("\tDebug:", debug)
		print("}")

		# Clock
		clock = _pygame.time.Clock()

		# Fonts
		font_fps = _pygame.font.Font(None, 50)
		
		# Loop
		while True:

			# Checking if the X button is pressed then the windows closed
			for event in _pygame.event.get():
				if event.type == _pygame.QUIT:
					self.exit()

			# User Loop
			if loop != None:
				loop()

			# Drawing on the window
			self.window.fill(self.window_background_color)
			if self.window_background_image != None:
				self.window.blit(self.window_background_image, (0, 0))

			for sprite in self.sprites:
				if sprite.visible:
					self.window.blit(sprite.image, (sprite.x, sprite.y))
			for rect in self.rects:
				if rect.visible:
					_pygame.draw.rect(self.window, rect.color, rect)
			for circle in self.circles:
				if circle.visible:
					_pygame.draw.ellipse(self.window, circle.color, circle)
			for button in self.buttons:
				if button.visible:
					button_rect = [button.x, button.x, button.width, button.height]
					
					if button._get_draw():
						_pygame.draw.rect(self.window, button.hover_color, button_rect)
					else:
						_pygame.draw.rect(self.window, button.color, button_rect)
			for txt in self.texts:
				if txt.visible:
					if txt.center:
						self.window.blit(txt.font.font_main.render(txt.title, False, txt.color), (txt.x-txt.label.get_width()/2, txt.y-txt.label.get_height()/2))
					else:
						self.window.blit(txt.font.font_main.render(txt.title, False, txt.color), (txt.x, txt.y))
			for line in self.lines:
				if line.visible:
					_pygame.draw.line(self.window, line.color, line.pos1, line.pos2, 2)

			# Drawing the fps
			if self.showing_fps:
				current_fps = font_fps.render(str(int(clock.get_fps())), False, (255, 255, 255))
				self.current_fps = current_fps
				self.window.blit(current_fps, (5, 5))

			# Updating the window
			_pygame.display.update()
			clock.tick(self.fps)

	# Exitting the application
	def exit(self):
		print("Exitting...")
		_pygame.quit()
		_sys.exit()
