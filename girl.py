# Copyright Vinicius Castanheira (vncastanheira@gmail.com) - 2012
#	This program is a part of the Noir Game.
# This program is under the Gnu LGPL.

from pygame import *
from pyganim import *
from entity import Entity

class Girl(Entity):
	def __init__(self, x, y, images):
		Entity.__init__(self, x, y, images)
		self.coliding = False
		self.alive = True

		self.dead = PygAnimation([("girl_dead.png", 0.5)])

	def draw(self, display):
		if self.alive:
			self.animation.play()
			self.animation.blit(display, (self.rect.x,self.rect.y))
		else:
			self.dead.play()
			self.dead.blit(display, (self.rect.x,self.rect.y))

	def collision(self, player):
		if sprite.collide_rect(self, player):
			self.coliding = True
			return
		self.coliding = False
		