from pygame import *
from pyganim import *
from entity import Entity
from bullet import Bullet

class Player(Entity):

	def __init__(self, x, y, images):
		Entity.__init__(self, x, y, images)
		# Properties
		self.alive = True
		self.isHidden = True
		self.bullets = 6
		# Directions variables
		self.goLeft = self.goRight = False
		self.facingDirection = 'RIGHT'
		# An exclamation mark, showing that the player is visible
		self.exclamation = Entity(self.rect.centerx, self.rect.top + 16, ["exclamation.png"])
		# Group of bullets objects, for updating and drawing
		self.bulletGroup = sprite.Group()
		# Dead animation
		self.animationDead = PygAnimation([("player_dead.png", 0.5)])

	def events(self, event):
		if self.alive:
			if event.type == KEYDOWN and event.key == K_RIGHT:
				self.goRight = True
				self.goLeft = False
				if self.facingDirection == 'LEFT':
					self.flip()
					self.facingDirection = 'RIGHT'
			if event.type == KEYDOWN and event.key == K_LEFT:	
				self.goRight = False
				self.goLeft = True
				if self.facingDirection == 'RIGHT':
					self.flip()
					self.facingDirection = 'LEFT'
			if event.type == KEYDOWN and event.key == K_z and not self.isHidden and self.bullets > 0:
				shoot = mixer.Sound("shoot.ogg")
				shoot.play()
				bulletDirection = 0
				if self.facingDirection == 'RIGHT':
					bulletDirection = self.rect.right
				if self.facingDirection == 'LEFT':
					bulletDirection = self.rect.left
				self.bulletGroup.add(Bullet(bulletDirection, self.rect.centery, self.facingDirection, ["bullet.png"]))
				self.bullets -= 1

			if event.type == KEYUP and event.key == K_RIGHT:
				self.goRight = False
			if event.type == KEYUP and event.key == K_LEFT:
				self.goLeft = False


	def update(self):
		movement = 4
		if self.alive:
			if self.rect.centerx - movement <=0 :
				self.rect.centerx = 4
			if self.goRight:
				self.move(movement,0)
			if self.goLeft:
				self.move(-movement,0)
			if self.rect.centerx >= 640:
				return 'NEXTLEVEL'

	def draw(self, display):
		if self.alive:
			self.animation.play()
			self.animation.blit(display, (self.rect.x,self.rect.y))
			if not self.isHidden:
				self.exclamation.animation.play()
				self.exclamation.animation.blit(display, (self.rect.centerx - 4, self.rect.top - 20))
		else:
			self.animationDead.play()
			self.animationDead.blit(display, (self.rect.x,self.rect.y))

	# Another functions

	def flip(self):
		self.animation.flip(True, False)

	def spotlightCollision(self, spolight):
		if sprite.collide_rect(self, spolight):
			self.isHidden = False
			return True
		else:
			self.isHidden = True
			return False

	def bulletCollision(self, bullet):
		if sprite.collide_rect(self, bullet) and not self.isHidden and self.alive:
			die = mixer.Sound("dead.ogg")
			die.play()
			self.alive = False
			return True # Collision occurred
		return False # Otherwise

			
