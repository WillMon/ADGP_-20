import sys, pygame
pygame.init()

size = width, height = 320, 240
squear = width,height = 17, 15
speed = [2, 2]
black = 255, 255, 255

screen = pygame.display.set_mode(size)
box = pygame.display.set_mode(squear)

#ball = pygame.image.load("fed.gif")
ballrect = ball.get_rect()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		
	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()