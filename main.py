# Noir Game
# A strategy-stealth shooter
	
# By Vinicius Castanheira (vncastanheira@gmail.com)
# This a free software and can be redistributed without charge.
# All code included can be used for your projects.

# Pyganim is a free module by Al Sweigart (al@inventwithpython.com)
# for doing simple 2D animation with Pygame.

from pygame import *
from entity import Entity
from player import Player
from enemy import Enemy
import leveldesign
from font_pallet import fontPallet
import pygame._view
import sys

SCREEN = (640, 480) # Resolution
FPS = 30

class Main:

	def __init__(self, SCREEN):
		# Initiate pygame and display.
		init()
		display.init()
		# Initiate the mixer for sounds and music
		mixer.init()
		mixer.music.load("jazz.ogg")
		mixer.music.play(-1)
		# Level number
		self.levelNumber = 1
		# Font object, to print font
		self.fontBig = fontPallet(8*3,"font_big.png")
		self.fontSmall = fontPallet(8,"font_small.png")
		# Create fps and set main display.
		self.fpsClock = time.Clock()
		self.mainDisplay = display.set_mode(SCREEN)
		# HUD
		self.HUD = Entity(300, 30, ["gun.png"])
		# Player Evilness
		self.playerEvilness = 0

		self.isNextLevel = False

	def playerEvent(self):
		for eventput in event.get():
			if eventput.type == KEYDOWN and eventput.key == K_ESCAPE:
				return 'QUIT'
			if eventput.type == KEYDOWN and eventput.key == K_r:
				level.restartLevel()
			if level.level == 7:
				if eventput.type == KEYDOWN and eventput.key == K_x:
					if level.boss.coliding:
						mixer.Sound("boss_girl_killed.ogg").play()
						level.boss.alive = False
						self.playerEvilness += 50
					if level.girl.coliding:
						mixer.Sound("boss_girl_killed.ogg").play()
						level.girl.alive = False
						self.playerEvilness += 100
					if level.money.coliding:
						mixer.Sound("take_money.ogg").play()
						level.money.taken = True
						self.playerEvilness += 70
			level.player.events(eventput)
			
	# Updates variables
	def update(self):
		if level.player.update() == 'NEXTLEVEL':
			self.isNextLevel = True
		for each_spotlight in level.spotlightGroup:
			if level.player.spotlightCollision(each_spotlight):
				break
		for each_bullet in level.player.bulletGroup:
				each_bullet.update()
		for each_enemy in level.enemyGroup:
			each_enemy.update(level.player)
			for each_bullet in level.player.bulletGroup:
				if each_enemy.bulletCollision(each_bullet):
					self.playerEvilness += 2
					level.player.bulletGroup.remove(each_bullet)
			for each_bullet in each_enemy.bulletGroup:
				each_bullet.update()
				if level.player.bulletCollision(each_bullet):
					if self.playerEvilness > 0:
						self.playerEvilness -= 5
					each_enemy.bulletGroup.remove(each_bullet)
		if level.level == 7:
			level.boss.collision(level.player)
			level.girl.collision(level.player)
			level.money.collision(level.player)


	# Draws to the screen when finished
	def draw(self):
		self.mainDisplay.fill((0,0,0))
		
		for each_enemy in level.enemyGroup:
			each_enemy.draw(self.mainDisplay)
			each_enemy.bulletGroup.draw(self.mainDisplay)
		if level.level == 7:
			level.boss.draw(self.mainDisplay)
			level.girl.draw(self.mainDisplay)
			if level.boss.alive:
				self.fontSmall.printf(self.mainDisplay, "Take my money, but",(220, 150))
				self.fontSmall.printf(self.mainDisplay, "please do not kill me!",(220, 160))
				if level.boss.coliding:
					self.fontBig.printf(self.mainDisplay, "Press X to execute!",(30, 65))
			if level.girl.alive:
				self.fontSmall.printf(self.mainDisplay, "Oh Lord, let me live!",(430, 160))
				if level.girl.coliding:
					self.fontBig.printf(self.mainDisplay, "Press X to execute!",(30, 65))
			if not level.money.taken:
				level.money.draw(self.mainDisplay)
				if level.money.coliding:
					self.fontBig.printf(self.mainDisplay, "Press X to take!",(30, 65))

		self.fontBig.printf(self.mainDisplay, "Evilness: " + str(self.playerEvilness), (50, 400))

		if level.level != 8:
			level.player.draw(self.mainDisplay)
			level.player.bulletGroup.draw(self.mainDisplay)
			level.floorGroup.draw(self.mainDisplay)
			level.spotlightGroup.draw(self.mainDisplay)

		# About the game and information
		if level.level == 1:
			self.fontBig.printf(self.mainDisplay,"Noir Game", (30,30))
			self.fontSmall.printf(self.mainDisplay,"   Read the README.txt instructions and history", (30, 70))
			self.fontSmall.printf(self.mainDisplay,"   Esc button quits the game", (30, 80))
			self.fontSmall.printf(self.mainDisplay,"   Z button to fire.", (30, 100))
			self.fontSmall.printf(self.mainDisplay,"   Left and Right arrows to move.", (30, 90))


		# Gun information
		if level.level != 8:
			self.HUD.animation.play()
			self.HUD.animation.blit(self.mainDisplay, (40, 300))
			self.fontSmall.printf(self.mainDisplay, "x" + str(level.player.bullets), (110, 330))
			if level.player.alive:
				self.fontSmall.printf(self.mainDisplay,"Status: ALIVE", (200, 330))
			else:
				self.fontSmall.printf(self.mainDisplay,"Status: DEAD", (200, 330))
				self.fontSmall.printf(self.mainDisplay,"R button restarts the level", (200, 350))

		# Game ending
		if level.level == 8:
			# Not taking anything
			if level.boss.alive and level.girl.alive and not level.money.taken:
				self.fontBig.printf(self.mainDisplay,"You leave at peace,", (20, 30))
				self.fontBig.printf(self.mainDisplay, "letting those people live.", (20, 60))
				self.fontBig.printf(self.mainDisplay,"You do not need that.", (20, 90))
				self.fontBig.printf(self.mainDisplay,"You made enough evil", (20, 120))
				self.fontBig.printf(self.mainDisplay,"for the day.", (20, 150))
			# Killing the old man only
			if not level.boss.alive and level.girl.alive and not level.money.taken:
				self.fontBig.printf(self.mainDisplay,"He is much of a nice", (20, 30))
				self.fontBig.printf(self.mainDisplay,"old man. You do not", (20, 60))
				self.fontBig.printf(self.mainDisplay,"like old mans.", (20, 90))
				self.fontBig.printf(self.mainDisplay,"But you do not need", (20, 120))
				self.fontBig.printf(self.mainDisplay,"this miserable money.", (20, 150))
				self.fontBig.printf(self.mainDisplay,"It is time to get some ", (20, 180))
				self.fontBig.printf(self.mainDisplay,"real cash!", (20, 210))
			# Killing both, but not taking the money
			if not level.boss.alive and not level.girl.alive and not level.money.taken:
				self.fontBig.printf(self.mainDisplay,"This is no real money!",(20, 30))
				self.fontBig.printf(self.mainDisplay,"You need big cash!",(20, 60))
				self.fontBig.printf(self.mainDisplay,"This was waste of time.",(20, 90))
				self.fontBig.printf(self.mainDisplay,"And you do not like",(20, 120))
				self.fontBig.printf(self.mainDisplay,"cyring babies, so you",(20, 150))
				self.fontBig.printf(self.mainDisplay,"end their miserable lives",(20, 180))
				self.fontBig.printf(self.mainDisplay,"without mercy! Yeah!",(20, 210))
			# Killing and taking everything
			if not level.boss.alive and not level.girl.alive and level.money.taken:
				self.fontBig.printf(self.mainDisplay,"People are so weak,",(20, 30))
				self.fontBig.printf(self.mainDisplay,"praying for their lives",(20, 60))
				self.fontBig.printf(self.mainDisplay,"as if it worth shit.",(20, 90))
				self.fontBig.printf(self.mainDisplay,"At least you got the",(20, 120))
				self.fontBig.printf(self.mainDisplay,"money.",(20, 150))
				self.fontBig.printf(self.mainDisplay,"Time to go for another",(20, 180))
				self.fontBig.printf(self.mainDisplay,"killing adventure!",(20, 210))
			# Killing only the girl
			if level.boss.alive and not level.girl.alive and not level.money.taken:
				self.fontBig.printf(self.mainDisplay,"Trading his life for,",(20, 30))
				self.fontBig.printf(self.mainDisplay,"the money, you let him",(20, 60))
				self.fontBig.printf(self.mainDisplay,"live. ",(20, 90))
				self.fontBig.printf(self.mainDisplay,"But since this is crappy",(20, 120))
				self.fontBig.printf(self.mainDisplay,"money, you leave it.",(20, 150))
				self.fontBig.printf(self.mainDisplay,"And since you do not ",(20, 180))
				self.fontBig.printf(self.mainDisplay,"stand crying bitches,",(20, 210))
				self.fontBig.printf(self.mainDisplay,"you killed her!",(20, 240))
			# Killing the girl and taking the money
			if level.boss.alive and not level.girl.alive and level.money.taken:
				self.fontBig.printf(self.mainDisplay,"You leave with a smile,",(20, 30))
				self.fontBig.printf(self.mainDisplay,"and thank him for the",(20, 60))
				self.fontBig.printf(self.mainDisplay,"money. ",(20, 90))
				self.fontBig.printf(self.mainDisplay,"And this girl needs to",(20, 120))
				self.fontBig.printf(self.mainDisplay,"shut up, what an awful",(20, 150))
				self.fontBig.printf(self.mainDisplay,"voice!",(20, 180))
				self.fontBig.printf(self.mainDisplay,"So, you did her this",(20, 210))
				self.fontBig.printf(self.mainDisplay,"kindly favor!",(20, 240))
			# Killing the boss and taking the money
			if not level.boss.alive and level.girl.alive and level.money.taken:
				self.fontBig.printf(self.mainDisplay,"Pathetic old man,",(20, 30))
				self.fontBig.printf(self.mainDisplay,"thinking you are",(20, 60))
				self.fontBig.printf(self.mainDisplay,"gonna spare him.",(20, 90))
				self.fontBig.printf(self.mainDisplay,"But you let the girl",(20, 120))
				self.fontBig.printf(self.mainDisplay,"live. At least ",(20, 150))
				self.fontBig.printf(self.mainDisplay,"she is hot.",(20, 180))
				self.fontBig.printf(self.mainDisplay,"Finally, the money",(20, 210))
				self.fontBig.printf(self.mainDisplay,"is all yours!",(20, 240))

	# Main loop. Everything in order.
	def loop(self,FPS):
		while True:
			level.playLevel()
			if (self.playerEvent() == 'QUIT'):
				quit()
				sys.exit()

			self.update()
			self.draw()
			if self.isNextLevel:
				level.nextLevel()
				self.isNextLevel = False
			display.update()
			self.fpsClock.tick(FPS)

# Creates a level object, with the level number as parameter
level = leveldesign.LevelDesign(1)
level.startLevel() # Initiate the level
main = Main(SCREEN) # Creates the Main Class with SCREEN
main.loop(FPS) # Loops with n FPS