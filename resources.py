import soundutil
import pygame
class Player:
	def __init__(self, pos, s):
		self.position = pygame.Vector3(pos[:])
		self.listener = soundutil.Listener(pos, s)
		self.soundSource = soundutil.SoundSource(pos, self.listener)
		self.row = 0
		
	def move(self, vel, dt):
		self.row += vel
		velo = pygame.Vector3(0,8,3)*vel
		self.position += velo
		self.listener.move(velo,dt)
		self.soundSource.move(velo,dt)
	def flash(self, eList):
		for e in eList:
			if e.position[1] == self.position[1]:
				if e.position[0] < 4 or self.position[0] > -4:
					e.isCaptured = True
					print("Captured")
					self.soundSource.play("assets/success.wav")
		self.soundSource.play("assets/flash.wav")
	
class Enemy:
	def __init__(self, pos, sp, s):
		self.position = pygame.Vector3(pos[:])
		self.speed = pygame.Vector3(sp[:])
		self.sound = s
		self.isCaptured = False
		self.isDead = False
	def move(self, vel,dt):
		self.position += vel
		self.sound.move(vec2tuple(vel),dt)
	def update(self, dt):
		self.move(self.speed,dt)
		if self.position[0] > 20:
			self.isDead = True
def vec2tuple(v):
	return (v[0],v[1],v[2])
