import random
import soundutil
import Tolk
import pygame
import game_util
import libaudioverse
from resources import *

libaudioverse.initialize()
game_util.start((800,600))
server = libaudioverse.Server()
server.set_output_device("default")
player = Player((0,0,0), server)
enemies = []
done = False
clock = pygame.time.Clock()
spawnValue = 6
dt = 0.0
ePath = ["assets/run.wav","assets/monkey.wav"]
eSpeed = (1,0,0)
score = 0
rChances = 5
#print(player.position)

while not done:
	dt = clock.tick()/1000
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		done =True
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			done = True
		elif event.key == pygame.K_UP and player.row < 2:
			player.move(1,dt)
			player.soundSource.play("assets/up.wav")
		elif event.key == pygame.K_DOWN and player.row > 0:
			player.move(-1,dt)
			player.soundSource.play("assets/down.wav")
		elif event.key == pygame.K_SPACE:
			player.flash(enemies)
			print("Player Position:",player.position)
	chance = random.randint(1, 20)
	spawnValue -= 1*dt
	if spawnValue < 0 and chance > 18:
		eRow = random.randint(0,2)
		ePos = (-20, eRow*8, eRow*3)
		e = Enemy(ePos, eSpeed, soundutil.SoundSource(ePos,player.listener))
		enemies.append(e)
		if e.position[1] == 16:
			e.sound.play(ePath[1], True)
		else:
			e.sound.play(ePath[0], True)
		spawnValue = 4
	for en in enemies:
		en.update(dt)
		print(en.position)
	i = 0
	while i  < len(enemies):
		if enemies[i].isCaptured == True:
			del enemies[i]
			score += 1
			print("Hit",score)
		elif enemies[i].isDead == True:
			del enemies[i]
			rChances -= 1
		else:
			i += 1
		
	if rChances <= 0:
		done = True

print("your score is",score)
game_util.end()
libaudioverse.shutdown()