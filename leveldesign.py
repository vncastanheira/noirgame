from pygame import *
from pyganim import *
from entity import Entity
from player import Player
from boss import Boss
from girl import Girl
from money import Money
from enemy import Enemy

class LevelDesign(object):	
	def __init__(self, number):
		self.level = number
		self.startingLevel = False 

		self.boss = None
		self.girl = None
		self.enemyGroup = sprite.Group()
		self.spotlightGroup = sprite.Group()

	def startLevel(self):
		self.startingLevel = True
		self.enemyGroup.empty()
		self.spotlightGroup.empty()

	def nextLevel(self):
		self.level += 1
		self.startLevel()

	def playLevel(self):
		if self.startingLevel:
			if self.level == 1:
				self.level_1()
			if self.level == 2:
				self.level_2()
			if self.level == 3:
				self.level_3()
			if self.level == 4:
				self.level_4()
			if self.level == 5:
				self.level_5()
			if self.level == 6:
				self.level_6()
			if self.level == 7:
				self.level_7()
			if self.level == 8:
				self.level_8()
			self.startingLevel = False

	def restartLevel(self):
		self.startLevel()
		self.playLevel()

	def level_1(self):
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])

		# Enemies
		self.enemyGroup.add(Enemy(300, 200,["enemy_standing.png", "enemy_walking.png"]))

		# Spotlights
		self.spotlightGroup.add(Entity(300, 200, ["spotlight.png"]))

		#Floors
		self.setFloor()

	def level_2(self):
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])

		# Enemies
		
		self.enemyGroup.add(Enemy(250, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(300, 200,["enemy_standing.png", "enemy_walking.png"]))

		# Spotlights
		self.spotlightGroup.add(Entity(275, 200, ["spotlight.png"]))

		#Floors
		self.setFloor()

	def level_3(self):
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])

		# Enemies
		
		self.enemyGroup.add(Enemy(200, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(232, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(264, 200,["enemy_standing.png", "enemy_walking.png"]))

		# Spotlights
		self.spotlightGroup.add(Entity(200, 200, ["spotlight.png"]))
		self.spotlightGroup.add(Entity(264, 200, ["spotlight.png"]))

		#Floors
		self.setFloor()

	def level_4(self):
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])

		# Enemies
		
		self.enemyGroup.add(Enemy(200, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(400, 200,["enemy_standing.png", "enemy_walking.png"]))

		# Spotlights
		self.spotlightGroup.add(Entity(200, 200, ["spotlight.png"]))
		self.spotlightGroup.add(Entity(400, 200, ["spotlight.png"]))

		#Floors
		self.setFloor()

	def level_5(self):
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])

		# Enemies
		
		self.enemyGroup.add(Enemy(200, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(400, 200,["enemy_standing.png", "enemy_walking.png"]))

		# Spotlights
		self.spotlightGroup.add(Entity(328, 200, ["spotlight.png"]))

		#Floors
		self.setFloor()

	def level_6(self):
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])

		# Enemies
		
		self.enemyGroup.add(Enemy(180, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(232, 200,["enemy_standing.png", "enemy_walking.png"]))
		self.enemyGroup.add(Enemy(464, 200,["enemy_standing.png", "enemy_walking.png"]))

		# Spotlights
		self.spotlightGroup.add(Entity(330, 200, ["spotlight.png"]))
		self.spotlightGroup.add(Entity(464, 200, ["spotlight.png"]))

		#Floors
		self.setFloor()

	def level_7(self):
		
		# Player
		self.player = Player(100, 200,["player_standing.png", "player_walking.png"])
		self.boss = Boss(280, 200, ["boss_1.png", "boss_2.png", "boss_3.png"])
		self.girl = Girl(500, 200, ["girl_1.png", "girl_2.png"])
		self.money = Money(550, 210, ["money.png"])

		# Set Floor
		self.setFloor()

	def level_8(self):
		self.player = Player(0, 500,["player_standing.png", "player_walking.png"])

	def setFloor(self):
		self.floorGroup = sprite.Group()
		for x in range(0,21):
			self.floorGroup.add(Entity(x*32, 240, ["floor.png"]))