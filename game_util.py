import pygame

def start(size):
	pygame.init()
	pygame.font.init()
	s= pygame.display.set_mode(size)
	return s
def end():
	pygame.font.quit()
	pygame.quit()