class Node(object):
	#What a node is defined as 
	def __init__(self,x = 0, y=0):
		
		self.x = x
		self.y = y
		self.Index = 0
		self.parent = None
		self.walk = True
		self.G = 0
		self.H = 0
		self.F = self.G + self.H
		
	'''def setF(self):
		self.F = self.G + self.H
	def getH(self):
		tempNode = Node()
		count = 0
	def getG(self, c_grid):
		for n in c_grid:
			++count'''
		
		
	#nl.sort(key lambda x: x: x.f)
class AStar(object):
	#AStar Constructer 
	def __init__(self,Start, End, searchSpace):
		self.Openl = []
		self.closeL = []		
		self.searchSpace = searchSpace
		self.Start = Start
		self.End = End 
		self.currentNode = self.Start
		self.pathDone = True
		
		
	#Checks for walkable Nodes 
	def unWalkable(self):
		for n in self.searchSpace:
			if n.x == 0 or n.x == ((len(self.searchSpace)/len(self.searchSpace)) - 1):
				n.walk = False
			if n.y == 0 or n.y == ((len(self.searchSpace)/len(self.searchSpace)) - 1):
				n.walk = False
			else:
				n.walk =  True
	def AddStartingNode(self):
		self.Openl.append(self.Start)
	
	def LowestF(self):
		lowestF = -1 
		nodeWithLowestF = None
		for n in self.Openl:
			lowestF =  n.F
			nodeWithLowestF = n 
		self.currentNode = nodeWithLowestF
	
	'''#Sets current node to its adjacent 
	def adjParent(self):
		for n in self.Openl:
			if not n == self.currentNode:
				n.parent = currentNode'''
				
	# Places current nodes adjacents in the Open List
	#aslong as its walkable or not already in the Open List  			
	def adj(self):
  		adjHolder = []
		rowL = 10
		
		adjHolder.append(self.currentNode)
 		adjHolder.append(self.searchSpace[self.currentNode.Index - rowL])
		adjHolder.append(self.searchSpace[self.currentNode.Index + rowL])
		adjHolder.append(self.searchSpace[self.currentNode.Index + 1])
		adjHolder.append(self.searchSpace[self.currentNode.Index - 1])
		adjHolder.append(self.searchSpace[self.currentNode.Index + rowL + 1])
 		adjHolder.append(self.searchSpace[self.currentNode.Index + rowL - 1])
 		adjHolder.append(self.searchSpace[self.currentNode.Index - rowL + 1])
 		adjHolder.append(self.searchSpace[self.currentNode.Index - rowL - 1])
 		
		ph = set(adjHolder)
		ol = set(self.Openl)
		
		for ah in adjHolder:
			if(not ah.walk or not ph.intersection(ol)):
				ah.parent = self.currentNode
				self.Openl.append(ah)
 	
	#Sets the adjacent Nodes G Coast 	
	def adjGcost(self):
		for ol in self.Openl:
			
			if abs(ol.Index - self.current.Index)  == 11 or abs(ol.Index - self.current.Index) == 9 :
				ol.G = 14
			else:
				ol.G = 10
	
	'''def closeL(self):
		self.closeL.append(currentNode)'''
		
	
	#Uses the Manhattan Formula to set the H for the nodes in the Search Space
	def ManhattanDis(self):
		for n in self.searchSpace:
			n.H = 10*(abs(n.x - self.End.x) + abs(n.y - self.End.y))
	
	def PrintInfo(self):
		for n in self.Openl:
			print("Oi")
	
	