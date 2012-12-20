# Copyright Vinicius Castanheira (vncastanheira@gmail.com) - 2012
#	This program is a part of the Noir Game.
# This program is under the Gnu LGPL.

import pygame
import pyganim

# Represents all moving entities on the game
# Non-moving stuff can have just a Sprite Group
# This class is meant to be extended
class Entity(pygame.sprite.Sprite):
	def __init__(self, x, y, images, width=0, height=0):
		# All sprite classes should extend pygame.sprite.Sprite.
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(images[0]) # First image as static
		self.rect = self.image.get_rect()
		if not (width == 0) or not (height == 0):
			self.rect.width = width
			self.rect.height = height
		self.rect.center = (x,y)

		# This is the main animation of any entity
		# Usally, when it's not moving or have only one animation
		self.animation = pyganim.PygAnimation([(frame, 0.5) for frame in images])

	# Don't know if those codes are useful
	def move(self, toX, toY):
		self.rect = self.rect.move(toX, toY)

	def destroy(self):
		pass

	def play(self):
		self.animation.play()

	def stop(self):
		self.animation.stop()
