
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

width = 30
pxlWidth = (25 * width) + 5
size = (pxlWidth, pxlWidth)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("A* Shortest Path")

done = False
clock = pygame.time.Clock()

#	Main Program loop
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.fill(WHITE)
	pygame.display.flip()
	clock.tick(60)
pygame.quite()
	
