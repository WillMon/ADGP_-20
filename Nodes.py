class Node(object):

	def __init__(self, x = 0, y=0):
		
		self.x = x
		self.y = y
		self.parent = None
		self.G = None
		self.H = None
		self.F = None
		
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

	def __init__(self, Start, End, Openl, surchSpace):
		self.Openl = []
		self.closeL = []		
		self.surchSpace = surchSpace
		self.Start = Start
		self.End = End 
		self.currentNode = self.Openl[self.Stat] 
		self.pathDone = false 
	
		
			
		
	def closeL(self):
		return self.closeL
		
		
	def adjParent(self):
		temp = []
		count = 0
		placeHolder = 0
		for n in self.surchSpace:
			++count 
		rowL = count/count 
		
		self.Openl.append(self.surchSpace[self.Start - rowL + 1])
		self.Openl.append(self.surchSpace[self.Start - rowL - 1])
		self.Openl.append(self.surchSpace[self.Start - rowl])
		self.Openl.append(self.surchSpace[self.Start + rowL + 1])
		self.Openl.append(self.surchSpace[self.Start + rowL - 1])
		self.Openl.append(self.surchSpace[self.Start + rowL])
		
		self.Openl.append(self.surchSpace[self.Start + 1])
		self.Openl.append(self.surchSpace[self.Start - 1])
		
		self.Openl.append(currentNode)
		
		self.Openl[0].parent = parent
		self.Openl[1].parent = parent
		self.Openl[2].parent = parent
		self.Openl[3].parent = parent
		self.Openl[4].parent = parent
		self.Openl[5].parent = parent
		
		
	def adjGcost(self):
		for n in self.surchSpace:
			if n.x == self.currentNode.x + 1 and n.y == self.currentNode.x + 1:
				n.g = currentNode.g + 14
			if n.x == self.currentNode.x - 1 and n.y == self.currentNode.x - 1:
				n.g = currentNode.g + 14
			if n.x == self.currentNode.x + 1 and n.y == self.currentNode.x - 1:
				n.g = currentNode.g + 14
			if n.x == self.currentNode.x - 1 and n.y == self.currentNode.x + 1:
				n.g = currentNode.g + 14
	
	
	
	
	
	def ManhatenDis(node1,node2):
		 if node1.x > node2.y or node1.x < node2:
			x_Axes = node1.x - node2.x
			if x_Axes < 0:x_Axes = -()x_Axes) 
			
		else if node1.y > node2.y or node1.y < node2.y:
			y_Axes = node1.y - node2.y
			if x_Axes < 0: y_Axes = -(y_Axes) 
			
		return x_Axes + y_Axes
	
	