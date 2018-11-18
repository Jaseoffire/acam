import pygame
pygame.init()
t1 = pygame.Vector2([3,2])
t2 = pygame.Vector2([1,1])
print(t1)
t1 += t2
print(t1)
print(t1[0])
print((t1+t2)[0])
print(t1)
t1 += t2*-1
print(t1)
pygame.quit()