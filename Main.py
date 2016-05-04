from Nodes import *

def main():
	searchSpace = []
	Start = Node(5,5)
	End = Node(9,9)
	count = 0
	for x in range(10):
		for y in range(10):
			n = Node(x,y, count)
			searchSpace.append(n)
			count += 1
			
	AStarGrid = AStar(searchSpace[4],searchSpace[76], searchSpace)	
	AStarGrid.AddStartingNode()		
	AStarGrid.unWalkable()
	AStarGrid.ManhattanDis()
	
	# while(not AStar.End in AStar.Openl)
	
	#while(not AStarGrid.pathDone):
	while(not AStarGrid.End in AStarGrid.Openl):
		AStarGrid.LowestF()
		AStarGrid.adj()
		AStarGrid.adjGcost()
		AStarGrid.ReachedGoel()
		AStarGrid.PrintInfo()
			
	'''print("Completed")
	pygame.init()
	WINDOW_SIZE = [255,255]
                        
	screen = pygame.display.set_mode(WINDOW_SIZE)
                        
	pygame.display.set_caption("ADGP_!20")
                        
	currentTime = pygame.time.get_ticks()
	print(currentTime)'''
	
main()





