from pygame import *
from pyganim import *
from entity import Entity
from bullet import Bullet
import random

class Enemy(Entity):
	
	def __init__(self, x, y, images):
		Entity.__init__(self, x, y, images)
		# Properties
		self.alive = True
		self.seeingPlayer = False
		self.originalPoint = x
		self.facingDirection = 'RIGHT'
		# Random direction purpose, max of 50
		self.delay = 0
		# Delay for shooting
		self.shootDelay = 10
		# Exclamation mark
		self.exclamation = Entity(self.rect.centerx, self.rect.top + 16, ["exclamation.png"])
		# Bullet group
		self.bulletGroup = sprite.Group()
		# Dead animation
		self.animationDead = PygAnimation([("enemy_dead.png", 0.5)])

	def update(self, player):
		if self.alive:
			movement = 4
			distance = self.rect.centerx - player.rect.centerx
			self.playerInSight(player)
			if not player.isHidden and self.seeingPlayer:
				self.shootDelay += 1
				if self.shootDelay > 10 and player.alive:
					bulletDirection = 0
					if self.facingDirection == 'RIGHT':
						bulletDirection = self.rect.right
					if self.facingDirection == 'LEFT':
						bulletDirection = self.rect.left
					shoot = mixer.Sound("shoot.ogg")
					shoot.play()
					self.bulletGroup.add(Bullet(bulletDirection, self.rect.centery, self.facingDirection, ["bullet.png"]))
					self.shootDelay = 0
				if abs(distance) < 100: 
					if distance > 0 and self.facingDirection == 'RIGHT':
						self.flip()
						self.facingDirection = 'LEFT'		
					if distance < 0 and self.facingDirection == 'LEFT':
						self.flip()
						self.facingDirection = 'RIGHT'
				if abs(distance) > 50 and abs(distance) < 100:
					if self.facingDirection == 'LEFT':
						movement *= -1
					self.move(movement, 0)
			else:
				if self.originalPoint < self.rect.centerx:
					if self.facingDirection == 'RIGHT':
						self.flip()
						self.facingDirection = 'LEFT'
					self.move(-movement, 0)
				if self.originalPoint > self.rect.centerx:
					if self.facingDirection != 'RIGHT':
						self.flip()
						self.facingDirection = 'RIGHT'
					self.move(movement, 0)
				if self.originalPoint == self.rect.centerx:
					if self.delay < 20:
						self.delay += 1
					else:
						if random.randint(1,2) == 1:
							if self.facingDirection == 'LEFT':
								self.flip()
							self.facingDirection = 'RIGHT'
						if random.randint(1,2) == 2:
							if self.facingDirection == 'RIGHT':
								self.flip()
							self.facingDirection = 'LEFT'
						self.delay = 0

		

	def draw(self, display):
		if self.alive:
			self.animation.play()
			self.animation.blit(display, (self.rect.x,self.rect.y))
			if self.seeingPlayer:
				self.exclamation.animation.play()
				self.exclamation.animation.blit(display, (self.rect.centerx - 4, self.rect.top - 20))
		else:
			self.animationDead.play()
			self.animationDead.blit(display, (self.rect.x,self.rect.y))

					
	def flip(self):
		self.animation.flip(True, False)

	def playerInSight(self, player):
		if ((self.facingDirection == 'RIGHT' and self.rect.centerx < player.rect.centerx) or \
		(self.facingDirection == 'LEFT' and self.rect.centerx > player.rect.centerx)) and not player.isHidden: 
			self.seeingPlayer = True
		else:
			self.seeingPlayer = False

	def bulletCollision(self, bullet):
		if sprite.collide_rect(self, bullet) and self.alive:
			die = mixer.Sound("kill.ogg")
			die.play()
			self.alive = False
			return True
		return False

