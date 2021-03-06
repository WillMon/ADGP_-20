import math 
from math import *


#Defines what a node consites of 
#Node Consites oh (x,y) its place in the array index
#It Point to it parent(another Node)
#Contains the G coast of the node 
#Contains the H = Manhattan Disatance 
# Contain the F = G + H
class Node(object):
	#What a node is defined as 
	def __init__(self,x = 0, y=0, index = 0):		
		self.x = x #X-axea 
		self.y = y #Y-axes  
		self.Index = index #Placement in the array 
		self.parent = None #Nodes parent Holder 
		self.walk = True   #
		self.symbol = "O"
		self.G = 0
		self.H = 0
		self.F = 0
		
	'''def setF(self):
		self.F = self.G + self.H
	def getH(self):
		tempNode = Node()
		count = 0
	def getG(self, c_grid):
		for n in c_grid:
			++count
		
	nl.sort(key lambda x: x: x.f)'''
class AStar(object):
	#AStar Constructer 
	
	def __init__(self,Start, End, searchSpace):
		self.Openl = []   #Holds nodes that meet t
		self.closeL = []	
		self.path = []
		self.searchSpace = searchSpace
		self.Start = Start
		self.End = End 
		self.currentNode = self.Start
		self.pathDone = False
		
		
	#Creaks a boundery by making the outside Nodes self.walk = false; 
	def unWalkable(self):
		for n in self.searchSpace:	#broke!!!!!!!!!!!!!!!!!!!!
			#self.searchSpace[55].walk = False
			if n.x == 0 or n.x == 9:
				n.walk = False
			elif  n.y == 0 or n.y == 9:
				n.walk = False
			else:
				n.walk =  True
		self.searchSpace[44].walk = False	
		self.searchSpace[34].walk = False	
	def AddStartingNode(self):
		self.Openl.append(self.Start)
		
	#Gathers the lowest F from the open list and replaces it with the current node 
	def Sort(self):
		for n in self.Openl:
			n.F = n.G + n.H
		sorted(self.Openl, key=lambda Node: Node.F)
	def LowestF(self):	
		self.closeL.append(self.Openl[0])
		self.currentNode = self.Openl[0]
		del self.Openl[0]
		
		
		'''lowestF = -1 
		nodeWithLowestF = None
		for n in self.Openl:
			if n.F > lowestF:
				lowestF =  n.F
				nodeWithLowestF = n 
		self.closeL.append(self.currentNode)		
		self.currentNode = nodeWithLowestF
		print nodeWithLowestF.Index		'''
	# Places current nodes adjacents in the Open List
	#aslong as its walkable or not already in the Open List  			
	def adj(self):
  		adjHolder = [] 
		rowL = 10
		#Appends adjacent nodes to the dummy array 
		adjHolder.append(self.currentNode.Index - rowL)
		adjHolder.append(self.currentNode.Index + rowL)
		adjHolder.append(self.currentNode.Index + 1)
		adjHolder.append(self.currentNode.Index - 1)
		adjHolder.append(self.currentNode.Index + rowL + 1)
 		adjHolder.append(self.currentNode.Index + rowL - 1)
 		adjHolder.append(self.currentNode.Index - rowL + 1)
 		adjHolder.append(self.currentNode.Index - rowL - 1)
		#Checks to see if to see that the index has not passed 0 & 100
		for ah in adjHolder:
			if ah >= 0 and ah < 100:
				if self.searchSpace[ah].walk and self.searchSpace[ah] not in self.closeL:
					if self.searchSpace[ah] not in self.Openl:
						self.Openl.append(self.searchSpace[ah])
						self.searchSpace[ah].parent = self.currentNode
						
				   	else:
						
						movecost = self.searchSpace[ah].G + self.currentNode.G
			   			if movecost < self.searchSpace[ah].G:
			   				self.searchSpace[ah].parent = self.currentNode
							self.searchSpace[ah].G = movecost
               
	#Sets the adjacent Nodes G Coast 	
	def adjGcost(self):
		for ol in self.Openl:
			if abs(ol.Index - self.currentNode.Index)  == 11 or abs(ol.Index - self.currentNode.Index) == 9 :
				ol.G = 14
			else:
				ol.G = 10

	#Uses the Manhattan Formula to set the H for the nodes in the Search Space
	def ManhattanDis(self):
		for n in self.searchSpace:
			n.H = 10*(abs(n.x - self.End.x) + abs(n.y - self.End.y))
	
	#Stops Loop Once the ending node is found in the end list 
	def ReachedGoel(self):
		if self.End in self.Openl:
			self.pathDone = False
			
	#Set the Symbold for the gride 
	def SetSymbols(self):
		for n in self.searchSpace:
			if n.walk == False:
				n.symbol = "="
			#Sets the symbol for the starting node 
			elif n == self.Start:
				n.symbol = "@"
			#Sets the symbol for the End node
			elif n == self.End:
				n.symbol = "X" 
			#Sets the Symbol for the path
			elif n in self.path:
				n.symbol = "#"	

	#Takes the parent of each node starting 
	#with the end node till it reaches the starting node
	#As it does that it adds it to the path list
	def Endpath(self):
		placeHolder = self.End
		while placeHolder != self.Start:
			self.path.append(placeHolder.parent)
			placeHolder = placeHolder.parent
			
	#Print out the gride structured for this project 
	def PrintInfo(self):
		for indx in self.searchSpace:
			if indx.x != 9: 
				print str(indx.symbol)  + "||",
			else:
				print str(indx.symbol) + "||"
			
		
		
		
		
		
