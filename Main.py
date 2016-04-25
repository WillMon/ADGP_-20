import pygame 
from Nodes import *

def main():
	searchSpace = []
	Start = Node(5,5)
	End = Node(9,9)
	count = 0
	for x in range(10):
		for y in range(10):
			n = Node(x,y)
			searchSpace.append(n)
			++count
	AStarGrid = AStar()		
			
			
		
	pygame.init()
	WINDOW_SIZE = [255,255]
	
	screen = pygame.display.set_mode(WINDOW_SIZE)
	
	pygame.display.set_caption("ADGP_!20")
	
	currentTime = pygame.time.get_ticks()
	print(currentTime)
	
main()





