# Noir Game
# A strategy-stealth shooter
	
# Copyright Vinicius Castanheira (vncastanheira@gmail.com) - 2012
#	This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.

# Pyganim is a free module by Al Sweigart (al@inventwithpython.com)
# for doing simple 2D animation with Pygame.

from pygame import *
from entity import Entity
from player import Player
from enemy import Enemy
import leveldesign
from font_pallet import fontPallet
from game_jolt_trophy import GameJoltTrophy
from trophy_ui import TrophyUI
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

		# Game Jolt Trophies User Interface
		self.trophyUI = TrophyUI()
		self.trophyUI.new('girl', ['not_so_fast_sweetheart.png'])
		self.trophyUI.new('oldman', ['you_lived_too_much.png'])
		self.trophyUI.new('money', ['no_empty_hands.png'])
		self.trophyUI.new('gun_light', ['only_a_gun_in_the_light.png'])
		self.bossTrophySet = False
		self.girlTrophySet = False
		self.moneyTrophySet = False
		self.gunlightTrophySet = False


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
		self.trophyUI.update()
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

		# Game Jolt Achievments
		if self.authSucess:
			if level.level == 7:

				if level.boss.alive == False:
					self.trophyUI.activate('oldman')
					if self.bossTrophySet == False:
						self.gameJolt.setTrophy('1151')
						self.bossTrophySet = True

				if level.girl.alive == False:
					self.trophyUI.activate('girl')
					if self.girlTrophySet == False:
						self.gameJolt.setTrophy('1152')
						self.girlTrophySet = True

				if level.money.taken == True:
					self.trophyUI.activate('money')
					if self.moneyTrophySet == False:
						self.gameJolt.setTrophy('1150')
						self.moneyTrophySet = True

			if self.playerEvilness >= 240:
				self.trophyUI.activate('gun_light')
				if self.gunlightTrophySet == False:
					self.gameJolt.setTrophy('1149')
					self.gunlightTrophySet = True



	# Draws to the screen when finished
	def draw(self):
		self.mainDisplay.fill((0,0,0))
		# Draw trohpies earned
		self.trophyUI.draw(self.mainDisplay)
		
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
			# Taking the money only.
			if level.boss.alive and level.girl.alive and level.money.taken:
				self.fontBig.printf(self.mainDisplay,"Dead people makes",(20, 30))
				self.fontBig.printf(self.mainDisplay,"so much mess!",(20, 60))
				self.fontBig.printf(self.mainDisplay,"And you do not ",(20, 90))
				self.fontBig.printf(self.mainDisplay,"want your hands",(20, 120))
				self.fontBig.printf(self.mainDisplay,"with dirty blood. ",(20, 150))
				self.fontBig.printf(self.mainDisplay,"You want the money,",(20, 180))
				self.fontBig.printf(self.mainDisplay,"So better take it",(20, 210))
				self.fontBig.printf(self.mainDisplay,"and just leave.",(20, 240))

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

	# Menu from the game, with buttons and authentication
	def menu(self):
		fontBig = fontPallet(8*3,"font_big.png")
		fontSmall = fontPallet(8,"font_small.png")
		username = ''
		user_token = ''
		usernameInputRect = Rect(200,220, 200, 14)
		usertokenInputRect = Rect(200,240, 200, 14)
		authBox = Rect(100, 260, 40, 30)
		usernameColor = (255,255,255)
		usertokenColor = (255,255,255)
		authenticationColor = (255,255,255)

		self.gameJolt = GameJoltTrophy(username, user_token, '11254', 'bc38e5418741cbd796217f97e86523b0')
		self.authSucess = None

		while True:
			self.mainDisplay.fill((0,0,0))
			for eventput in event.get():
				(x, y) = mouse.get_pos()

				# Esc key
				if eventput.type == KEYDOWN and eventput.key == K_ESCAPE:
					quit()
					sys.exit()

				# Mouse button
				if eventput.type == MOUSEBUTTONDOWN:
					(mouseleft, garbage1, garbage2) = mouse.get_pressed()
					if mouseleft and (x >= 100 and x <= 100+(8*3*len('Start'))) and (y >= 120 and y <= 120+(8*3)):
						return
					if mouseleft and (x >= 100 and x <= 100+(8*3*len('Start'))) and (y >= 330 and y <= 330+(8*3)):
						quit()
						sys.exit()
					if mouseleft and (x > 100 and x < 140) and (y >= 260 and y <= 290):
						self.gameJolt.changeUsername(username)
						self.gameJolt.changeUserToken(user_token)
						self.authSucess = self.gameJolt.authenticateUser()

				# Text input field
				try:
					if (x > 200 and x < 400) and (y >= 220 and y <= 234):
						if eventput.unicode != '\b':
							username += eventput.unicode
						else:
							username = username[:-1]
					if (x > 200 and x < 400) and (y >= 240 and y <= 254):
						if eventput.unicode != '\b':
							user_token += eventput.unicode
						else:
							user_token = user_token[:-1]
				except Exception:
					pass

				# Mouse motion
				if eventput.type == MOUSEMOTION:
					if (x > 200 and x < 400) and (y >= 220 and y <= 234):
						usernameColor = (255, 0, 0)
					else:
						usernameColor = (255, 255, 255)
					if (x > 200 and x < 400) and (y >= 240 and y <= 254):
						usertokenColor = (255, 0, 0)
					else:
						usertokenColor = (255, 255, 255)
					if (x > 100 and x < 140) and (y >= 260 and y <= 290):
						authenticationColor = (255, 0, 0)
					else:
						authenticationColor = (255,255,255)
			
			if self.authSucess == False:
				fontSmall.printf(self.mainDisplay, "Failed...", (160, 280))
			elif self.authSucess == True:
				fontSmall.printf(self.mainDisplay, "Sucess!", (160, 280))
			else:
				pass

			fontBig.printf(self.mainDisplay, 'Start', (100,120))
			fontSmall.printf(self.mainDisplay, 'Login on GameJolt:', (100,200))
			fontSmall.printf(self.mainDisplay, 'Username', (100, 220))
			fontSmall.printf(self.mainDisplay, 'User Token', (100, 235))
			fontSmall.printf(self.mainDisplay, 'OK!', (110, 270))
			draw.rect(self.mainDisplay, authenticationColor, authBox, 1)
			fontSmall.printf(self.mainDisplay, username, (200, 222))
			fontSmall.printf(self.mainDisplay, user_token, (200, 242))
			draw.rect(self.mainDisplay, usernameColor, usernameInputRect, 1)
			draw.rect(self.mainDisplay, usertokenColor, usertokenInputRect, 1)
			fontBig.printf(self.mainDisplay, 'Exit', (100,330))
			display.update()
			self.fpsClock.tick(FPS)


# Creates a level object, with the level number as parameter
level = leveldesign.LevelDesign(1)
level.startLevel() # Initiate the level
main = Main(SCREEN) # Creates the Main Class with SCREEN
main.menu()
main.loop(FPS) # Loops with n FPS