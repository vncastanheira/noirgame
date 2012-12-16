from pygame import *
from pyganim import *
from entity import Entity

class Money(Entity):
	def __init__(self, x, y, images):
		Entity.__init__(self, x, y, images)
		self.coliding = False
		self.taken = False

	def draw(self, display):
		self.animation.play()
		self.animation.blit(display, (self.rect.x,self.rect.y))

	def collision(self, player):
		if sprite.collide_rect(self, player):
			self.coliding = True
			return
		self.coliding = False
		