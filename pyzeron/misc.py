# Importing extensions and packages
import pygame as _pygame

# Initializing pygame
_pygame.init()

# Functions
# Loading an image
def load_image(file):
	return _pygame.image.load(file)

# Scaling an image
def scale_image(img, size):
	return _pygame.transform.scale(img, size)

# Flipping an image
def flip_image(img, horizontal, vertical):
	return _pygame.transform.flip(img, horizontal, vertical)

# Loading a sound
def load_sound(file):
	return _pygame.mixer.Sound(file)

# Loading the music
def load_music(file):
	return _pygame.mixer.music.load(file)

# Playing the music
def play_music():
	return _pygame.mixer.music.play(-1)

# Checking if objects are colliding
def collide_check(obj1, obj2):
	if obj1 == Sprite:
		return obj1.rect.colliderect(obj2)
	elif obj2 == Sprite:
		return obj1.colliderect(obj2.rect)
	elif obj1 == Spirte and obj2 == Sprite:
		return obj1.rect.colliderect(obj2.rect)

	return obj1.colliderect(obj2)

# Checking if mask of objects are colliding
def collide_mask_check(left, right):
	xoffset = right.x - left.x
	yoffset = right.y - left.y
	try:
		leftmask = left.mask
	except AttributeError:
		leftmask = _pygame.mask.from_surface(left.image)
	try:
		rightmask = right.mask
	except AttributeError:
		rightmask = _pygame.mask.from_surface(right.image)
	return leftmask.overlap(rightmask, (xoffset, yoffset))

# Button Event Decorator
def button_event():
	pass
