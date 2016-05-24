import sys, pygame
import Nodes 
from Nodes import *

def main():
	searchSpace = []
	Start = Node(5,5)
	End = Node(9,9)
	count = 0
	
	done = False
	single = [0,1,2,3,4,5,6,7,8,9]
	for x in range(10):
		for y in range(10):
			n = Node(x,y, count)
			searchSpace.append(n)
			count += 1
			
	AStarGrid = AStar(searchSpace[45],searchSpace[76], searchSpace)	
	AStarGrid.AddStartingNode()		
	AStarGrid.unWalkable()
	AStarGrid.ManhattanDis()
	
	# while(not AStar.End in AStar.Openl)
	
	#while(not AStarGrid.pathDone):
	while(not AStarGrid.End in AStarGrid.Openl):
		AStarGrid.adj()
		AStarGrid.LowestF()
		AStarGrid.adjGcost()
		AStarGrid.ReachedGoel()
	AStarGrid.Endpath()
	AStarGrid.ReachedGoel()
	
	
	AStarGrid.PrintInfo()
			
	print("Completed")
	'''pygame.init()
	WINDOW_SIZE = [255,255]
                        
	screen = pygame.display.set_mode(WINDOW_SIZE)
                        
	pygame.display.set_caption("ADGP_!20")
                        
	currentTime = pygame.time.get_ticks()
	print(currentTime)
	
	# -------- Main Program Loop -----------
	while not done:
		for event in pygame.event.get():  # User did something
			if event.type == pygame.QUIT:  # If user clicked close
				done = True	 # Flag that we are done so we exit this loop
	
	
	
	
		# Set the screen background
		screen.fill((0,0,0))
	
		for i in searchSpace:
			i.draw(screen, (255,255,255))
	
		# Limit to 60 frames per second
		clock.tick(60)
	
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
	
	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()'''
	
main()





