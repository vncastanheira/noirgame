from pygame import *
from entity import Entity
import sys

class TrophyUI(object):
	def __init__(self):
		self.frameCounter = 0
		# A list of trophies
		# Each trophie is a dictionary containing name, image and a Rect
		self.trophyList = []
		self.trophySpriteGroup = sprite.Group()
		
	def new(self, name, image):
		new = {}
		new['name'] = name
		new['entity'] = Entity(578,510, image)
		new['active'] = False
		new['timer'] = 0
		self.trophyList.append(new)
		self.trophySpriteGroup.add(new['entity'])

	def activate(self, name):
		for trophy in self.trophyList:
			if trophy['name'] == name:
				trophy['active'] = True
				print('Fround!')
				return

	def update(self):
		for trophy in self.trophyList:
			if trophy['active'] == True:
				print(trophy['timer'])
				if trophy['timer'] < 30:
					trophy['entity'].move(0,-2)
					trophy['timer'] += 1
				elif trophy['timer'] >= 30 and trophy['timer'] < 120:
					trophy['timer'] += 1
				elif trophy['timer'] == 120:
					trophy['timer'] = 0
					trophy['active'] = False
					trophy['entity'].move(0,510)

	def draw(self, mainDisplay):
		self.trophySpriteGroup.draw(mainDisplay)

"""
# Testing area
SCREEN = (640, 480) # Resolution
FPS = 30
init()
display.init()
mainDisplay = display.set_mode(SCREEN)
fpsClock = time.Clock()
trophyObject = TrophyUI()
trophyObject.newTrophy('girl_killed', ['not_so_fast_sweetheart.png'])

while True:
	mainDisplay.fill((0,0,0))
	for eventput in event.get():
		if eventput.type == KEYDOWN and eventput.key == K_ESCAPE:
			quit()
			sys.exit()
		if eventput.type == KEYDOWN and eventput.key == K_a:
			trophyObject.activateTrophy('girl_killed')
			print('Activate!')

	trophyObject.updateTrophies()
	trophyObject.drawTrophies(mainDisplay)
	display.update()
	fpsClock.tick(FPS)
"""