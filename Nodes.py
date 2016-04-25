class Node(object):

	def __init__(self, Index x = 0, y=0):
		
		self.x = x
		self.y = y
		self.Index = Index
		self.parent = None
		self.walk = True
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

	def __init__(self,Start, End, Openl, surchSpace):
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
		for n in self.surchSpace:
			if n.x == self.currentNode.x + 1 and n.y == self.self.currentNode.y:
				self.Openl.append(n)
			if n.x == self.currentNode.x - 1 and n.y == self.self.currentNode.y:
				self.Openl.append(n)	
			if n.y == self.currentNode.y + 1 and n.x == self.self.currentNode.x:
				self.Openl.append(n)
			if n.y == self.currentNode.y - 1 and n.x == self.self.currentNode.x:
				self.Openl.append(n)	
			if n.x == self.currentNode.x + 2 and n.y == self.self.currentNode.y:
				self.Openl.append(n)
			if n.x == self.currentNode.x - 2 and n.y == self.self.currentNode.y:
				self.Openl.append(n)	
			if n.y == self.currentNode.y + 2 and n.x == self.self.currentNode.x:
				self.Openl.append(n)
			if n.y == self.currentNode.y - 2 and n.x == self.self.currentNode.x:
				self.Openl.append(n)	
				
		self.Openl.append(currentNode)
		
		'''for n in self.surchSpace:
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
		
		self.Openl.append(currentNode)'''
		
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

				
	def ManhattanDis(node1,node2):
		return 10*(abs(node1.x-node2.x) + abs(node1.y-node2.y))
	
	
	
	