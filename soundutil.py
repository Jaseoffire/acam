import pygame
import libaudioverse

class SoundPlayer:
	def __init__(self, server):
		self.buffer_player = libaudioverse.BufferNode(server)
		self.file = ""
	def play(self, path, loop=False, pos=0.0):
		"""This function takes a path to an audio file. Optionally, you can add a boolean for looping and a starting position. It is ment to make playing files easier."""
		if self.file != path:
			tmp_buffer = libaudioverse.Buffer(self.buffer_player.server)
			tmp_buffer.load_from_file(path)
			self.buffer_player.buffer = tmp_buffer
		self.buffer_player.looping = loop
		self.buffer_player.position = pos
		self.buffer_player.connect(0, self.buffer_player.server)
	def pause(self):
		"""Allows the sound player to pause."""
		self.buffer_player.state = libaudioverse.NodeStates.paused
		
	def resume(self):
		"""Resumes the playback of a file."""
		self.buffer_player.state = libaudioverse.NodeStates.playing
	
class SoundSource(SoundPlayer):
	def __init__(self, pos, listener):
		"""For the position, this class is expecting a vector. A vector will work as intended, at any rate."""
		super().__init__(listener.server)
		self.position = pos
		self.source = libaudioverse.SourceNode(listener.server, listener.environment)
		self.source.position = tuple(pos)
		
	def play(self, path, loop=False, pos=0.0):
		"""This function takes a path to an audio file. Optionally, you can add a boolean for looping and a starting position. It is ment to make playing files easier. This is being pasted as the only thing that needs changed is the connect statement."""
		if self.file != path:
			tmp_buffer = libaudioverse.Buffer(self.buffer_player.server)
			tmp_buffer.load_from_file(path)
			self.buffer_player.buffer = tmp_buffer
		self.buffer_player.looping = loop
		self.buffer_player.position = pos
		self.buffer_player.connect(0, self.source, 0)
	def move(self, vel, dt):
		"""Moves the sound by adding whatever velocity vector you pass it."""
		pygame.Vector3(self.position)
		self.position += pygame.Vector3(vel)*dt
		self.source.position = tuple(self.position)
		
	
class Listener:
	def __init__(self, pos, s, oc=2, o=(0, 1, 0, 0, 0, 1)):
		"""Takes a server and a position (usually the position of the player) and sets the listener their. Optionally, takes a number of output channels."""
		self.position = pos
		self.environment = libaudioverse.EnvironmentNode(s, "default")
		self.environment.panning_strategy = libaudioverse.PanningStrategies.hrtf
		self.environment.output_channels = oc
		self.environment.position = tuple(pos)
		self.environment.orientation = tuple(o)
		#self.environment.default_size = 100.0
		self.environment.connect(0, s)
		self.server = s
	def move(self, vel, dt):
		"""Moves the listener."""
		pygame.Vector3(self.position)
		self.position += pygame.Vector3(vel)*dt
		self.environment.position = tuple(self.position)