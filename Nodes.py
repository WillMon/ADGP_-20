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
		closeL = []		
		self.Start = Start
		self.End = End 
		self.currentNode = self.Openl[self.Stat] 
		self.pathDone = false 
	
		
			
		
	def closeL(self):
		return self.closeL
		
		
	def adjParent(self):
		temp = []
		count= 0
		rowL = 0
		placeHolder = 0
		for n in self.Openl:
			++count 
		rowL = count/count 
		self.Openl[self.Start + rowL + 1].parent = self.currentNode
		self.Openl[self.Start + rowL - 1].parent = self.currentNode
		self.Openl[self.Start - rowL].parent = self.currentNode
		self.Openl[self.Start - rowL + 1].parent = self.currentNode
		self.Openl[self.Start - rowL - 1].parent = self.currentNode
		self.Openl[self.Start + 1].parent = self.currentNode
		self.Openl[self.Start - 1].parent = self.currentNode
		
	def adjGcost(self):
		for 
	
	