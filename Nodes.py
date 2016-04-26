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
		
	def setF(self):
		self.F = self.G + self.H
	def getH(self):
		tempNode = Node()
		count = 0
	def getG(self, c_grid):
		for n in c_grid:
			++count
		
		
	#nl.sort(key lambda x: x: x.f)
class AStar(object):
	#AStar Constructer 
	def __init__(self,Start, End, searchSpace):
		self.Openl = []
		self.closeL = []		
		self.searchSpace = searchSpace
		self.Start = Start
		self.End = End 
		self.currentNode = self.Openl[self.Stat] 
		self.pathDone = false 
	#Checks for walkable Nodes 
	def unWalkable(self):
		for n in self.searchSpace:
			if n.x == 0 or n.x == ((len(searchSpace)/len(searchSpace)) - 1):
				n.walk = False
			else if n.y == 0 or n.y == ((len(searchSpace)/len(searchSpace)) - 1):
				n.walk = False
			else:
				n.walk =  True
	#Sets current not to current nodes adjacent	from the Open List	
	def adjParent(self):
		for n in self.Openl:
			if not n == self.currentNode:
				n.parent = currentNode
	# Places current nodes in along with its adjacenta in the Open List form the searchSpace 			
	def adj(self):
		rowL = 0
 		count = 0
  		adjHolder []
 		for n in self.searchSpace:
  			++count 
  		rowL = count/count 
		
		adjHolder.append(self.currentNode)
 		adjHolder.append(self.searchSpace[self.currentNode.Index - rowL])
		adjHolder.append(self.searchSpace[self.currentNode.Index + rowL])
		adjHolder.append(self.searchSpace[self.currentNode.Index + 1])
		adjHolder.append(self.searchSpace[self.currentNode.Index - 1])
		adjHolder.append(self.searchSpace[self.currentNode.Index + rowL + 1])
 		adjHolder.append(self.searchSpace[self.currentNodet.Index + rowL - 1])
 		adjHolder.append(self.searchSpace[self.currentNode.Index - rowL + 1])
 		adjHolder.append(self.searchSpace[self.currentNode.Index - rowL - 1])
 		
 		
		for ah adjHolder:
			if ah.walk:
				self.Openl.append(ah)
 	
	#Sets the adajcent Nodes G Coast 	
	def adjGcost(self):
	
		count = 1
		for ol in self.Openl:
			
			if count < 5:
				ol.G = 10
			else:
				ol.G = 14
	
	def closeL(self):
		self.closeL.append(currentNode)
		
	
	#Uses the Manhattan Formula to set the H for the nodes in the Search Space
	def ManhattanDis(self):
		for n in self.searchSpace:
		n.H = 10*(abs(n.x - End.x) + abs(n.y - End.y))
	
	
	
	