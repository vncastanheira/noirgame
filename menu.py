from pygame import *
from font_pallet import fontPallet
from game_jolt_trophy import GameJoltTrophy
import sys


SCREEN = (640, 480) # Resolution
FPS = 30
init()
display.init()
mainDisplay = display.set_mode(SCREEN)
fpsClock = time.Clock()
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

gameJolt = GameJoltTrophy(username, user_token, '11254', 'bc38e5418741cbd796217f97e86523b0')
authSucess = None

while True:
	mainDisplay.fill((0,0,0))
	for eventput in event.get():
		(x, y) = mouse.get_pos()

		# Esc key
		if eventput.type == KEYDOWN and eventput.key == K_ESCAPE:
			quit()
			sys.exit()

		# Mouse button
		if eventput.type == MOUSEBUTTONDOWN:
			(mouseleft, garbage1, garbage2) = mouse.get_pressed()
			if mouseleft and (x >= 100 and x <= 100+(8*3*len('Start'))) and (y >= 100 and y <= 100+(8*3)):
				print('Start')
			if mouseleft and (x >= 100 and x <= 100+(8*3*len('Start'))) and (y >= 330 and y <= 330+(8*3)):
				quit()
				sys.exit()
			if mouseleft and (x > 100 and x < 140) and (y >= 260 and y <= 290):
				gameJolt.changeUsername(username)
				gameJolt.changeUserToken(user_token)
				authSucess = gameJolt.authenticateUser()
				print(str(username)+' - '+str(user_token))

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
	
	if authSucess == False:
		fontSmall.printf(mainDisplay, "Failed...", (160, 280))
	elif authSucess == True:
		fontSmall.printf(mainDisplay, "Sucess!", (160, 280))
	else:
		pass

	fontBig.printf(mainDisplay, 'Start', (100,120))
	fontSmall.printf(mainDisplay, 'Login on GameJolt:', (100,200))
	fontSmall.printf(mainDisplay, 'Username', (100, 220))
	fontSmall.printf(mainDisplay, 'User Token', (100, 235))
	fontSmall.printf(mainDisplay, 'OK!', (110, 270))
	draw.rect(mainDisplay, authenticationColor, authBox, 1)
	fontSmall.printf(mainDisplay, username, (200, 222))
	fontSmall.printf(mainDisplay, user_token, (200, 242))
	draw.rect(mainDisplay, usernameColor, usernameInputRect, 1)
	draw.rect(mainDisplay, usertokenColor, usertokenInputRect, 1)
	fontBig.printf(mainDisplay, 'Exit', (100,330))

	display.update()
	fpsClock.tick(FPS)