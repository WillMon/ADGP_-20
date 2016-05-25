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
			n = Node(y,x, count)
			searchSpace.append(n)
			count += 1
	start = raw_input("Enter Starting Value: ")
	end = raw_input("Enter Ending Value: ")
	AStarGrid = AStar(searchSpace[int(start)],searchSpace[int(end)], searchSpace)	
	AStarGrid.AddStartingNode()		
	AStarGrid.unWalkable()
	AStarGrid.ManhattanDis()
	
	while(not AStarGrid.End in AStarGrid.Openl):
		AStarGrid.LowestF()
		AStarGrid.adj()
		AStarGrid.Sort()
		AStarGrid.adjGcost()
		AStarGrid.ReachedGoel()

	'''for r in AStarGrid.closeL:
		print r.Index'''
		
	AStarGrid.Endpath()
	AStarGrid.SetSymbols()
	
	
	AStarGrid.PrintInfo()
			
	print("Completed")
	
main()
raw_input()




