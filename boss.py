from pygame import *
from pyganim import *
from entity import Entity

class Boss(Entity):
	def __init__(self, x, y, images):
		Entity.__init__(self, x, y, images)
		self.coliding = False
		self.alive = True

		self.dead = PygAnimation([("boss_dead.png", 0.5)])

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
		
