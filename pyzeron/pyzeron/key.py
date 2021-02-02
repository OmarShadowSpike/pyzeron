# Importing extensions and packages
import pygame
import sys
import random

# Initializing pygame
pygame.init()

# Checking if a key is held
def keyHold(key):
	keys = pygame.key.get_pressed()

	if key == "q":
		return keys[pygame.K_q]
	elif key == "w":
		return keys[pygame.K_w]
	elif key == "e":
		return keys[pygame.K_e]
	elif key == "r":
		return keys[pygame.K_r]
	elif key == "t":
		return keys[pygame.K_t]
	elif key == "y":
		return keys[pygame.K_y]
	elif key == "u":
		return keys[pygame.K_u]
	elif key == "i":
		return keys[pygame.K_i]
	elif key == "o":
		return keys[pygame.K_o]
	elif key == "p":
		return keys[pygame.K_p]
	elif key == "a":
		return keys[pygame.K_a]
	elif key == "s":
		return keys[pygame.K_s]
	elif key == "d":
		return keys[pygame.K_d]
	elif key == "f":
		return keys[pygame.K_f]
	elif key == "g":
		return keys[pygame.K_g]
	elif key == "h":
		return keys[pygame.K_h]
	elif key == "j":
		return keys[pygame.K_j]
	elif key == "k":
		return keys[pygame.K_k]
	elif key == "l":
		return keys[pygame.K_l]
	elif key == "z":
		return keys[pygame.K_z]
	elif key == "x":
		return keys[pygame.K_x]
	elif key == "c":
		return keys[pygame.K_c]
	elif key == "v":
		return keys[pygame.K_v]
	elif key == "b":
		return keys[pygame.K_b]
	elif key == "n":
		return keys[pygame.K_n]
	elif key == "m":
		return keys[pygame.K_m]
	elif key == "0":
		return keys[pygame.K_0]
	elif key == "1":
		return keys[pygame.K_1]
	elif key == "2":
		return keys[pygame.K_2]
	elif key == "3":
		return keys[pygame.K_3]
	elif key == "4":
		return keys[pygame.K_4]
	elif key == "5":
		return keys[pygame.K_5]
	elif key == "6":
		return keys[pygame.K_6]
	elif key == "7":
		return keys[pygame.K_7]
	elif key == "8":
		return keys[pygame.K_8]
	elif key == "9":
		return keys[pygame.K_9]
	elif key == "SPACE":
		return keys[pygame.K_SPACE]
	elif key == "ENTER":
		return keys[pygame.K_KP_ENTER]
	elif key == "BACKSPACE":
		return keys[pygame.K_BACKSPACE]
	elif key == "DEL":
		return keys[pygame.K_DELETE]
	elif key == "SHIFT":
		return keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
	elif key == "LSHIFT":
		return keys[pygame.K_LSHIFT]
	elif key == "RSHIFT":
		return keys[pygame.K_RSHIFT]
	elif key == "UP":
		return keys[pygame.K_UP]
	elif key == "DOWN":
		return keys[pygame.K_DOWN]
	elif key == "LEFT":
		return keys[pygame.K_LEFT]
	elif key == "RIGHT":
		return keys[pygame.K_RIGHT]
