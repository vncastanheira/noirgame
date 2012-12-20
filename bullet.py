# Copyright Vinicius Castanheira (vncastanheira@gmail.com) - 2012
#	This program is a part of the Noir Game.
# This program is under the Gnu LGPL.

import pygame
from entity import Entity

import math
class Bullet(Entity):
	def __init__(self, x, y, direction, image):
		Entity.__init__(self, x, y, image)
		self.direction = direction

	def update(self):
		speed = 10
		if self.direction == 'RIGHT':
			self.move(speed, 0)
		if self.direction == 'LEFT':
			self.move(-speed, 0)