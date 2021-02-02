# Importing extensions and packages
import pygame
import sys
import random

from .objects import Rect, Circle, Sprite
from .misc import *

# Initializing pygame
pygame.init()

# App class
class App():
	def __init__(self, title, width, height):
		self.windowSize = self.windowWidth, self.windowHeight = width, height
		self.windowTitle = title

		self.sprites = []
		self.rects = []
		self.circles = []
		self.texts = []

		self.windowBackgroundColor = (20, 20, 20)
		self.windowBackgroundImage = None
		self.showingFps = True

		self.window = pygame.display.set_mode(self.windowSize)
		pygame.display.set_caption(self.windowTitle)

	# Setting the window's background color
	def setBackgroundColor(self, color):
		self.windowBackgroundColor = color

	# Setting the window's background image
	def setBackgroundImage(self, image):
		self.windowBackgroundImage = image

	# Showing the fps
	def showFps(self):
		self.showingFps = True

	# Hiding the fps
	def hideFps(self):
		self.showingFps = False

	# Drawing sprites in the loop
	def _drawSprite(self, sprite):
		self.sprites.append(sprite)

	# Drawing rects in the loop
	def _drawRect(self, rect):
		self.rects.append(rect)

	# Drawing circles in the loop
	def _drawCircle(self, circle):
		self.circles.append(circle)

	# Drawing texts in the loop
	def _drawText(self, txt):
		self.texts.append(txt)

	# Drawing objects in the loop
	def draw(self, obj):
		if type(obj) == Sprite:
			self._drawSprite(obj)
		elif type(obj) == Rect:
			self._drawRect(obj)
		elif type(obj) == Circle:
			self._drawCircle(obj)

	# Drawing an entire list of objects
	def drawList(self, list):
		for obj in list:
			if type(obj) == Sprite:
				self._drawSprite(obj)
			elif type(obj) == Rect:
				self._drawRect(obj)
			elif type(obj) == Circle:
				self._drawCircle(obj)

	# Running the application
	def run(self, fps=60, inLoop=None, debug=False):
		print("Starting...")
		print("Stats:")
		print("{")
		print("\tFps:", fps)
		print("\tDebug:", debug)
		print("}")

		# Clock
		clock = pygame.time.Clock()

		# Fonts
		fontFps = pygame.font.Font(None, 50)
		
		# Loop
		while True:

			# Checking if the X button is pressed then the windows closed
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.exit()

			# Inloop
			if inLoop != None:
				inLoop()

			# Drawing on the window
			self.window.fill(self.windowBackgroundColor)
			if self.windowBackgroundImage != None:
				self.window.blit(windowBackgroundImage, (0, 0))

			for sprite in self.sprites:
				if sprite.visible:
					self.window.blit(sprite.image, sprite.x, sprite.y)
			for rect in self.rects:
				if rect.visible:
					pygame.draw.rect(self.window, rect.color, rect)
			for circle in self.circles:
				if circle.visible:
					pygame.draw.ellipse(self.window, circle.color, circle)

			# Drawing the fps
			if self.showingFps:
				currentFps = fontFps.render(str(int(clock.get_fps())), False, (255, 255, 255))
				self.window.blit(currentFps, (5, 5))

			# Updating the window
			pygame.display.update()
			clock.tick(fps)

	# Exitting the application
	def exit(self):
		print("Exitting...")
		pygame.quit()
		sys.exit()
