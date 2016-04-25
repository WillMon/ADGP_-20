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

	def __init__(self, Start, End, Openl):
		self.Openl = Openl
		self.Start = Start
		self.End = End 
		closeL = None
		pathDone = false 
	
	def Adj(self):
		temp = []
		count= 0
		rowL
		placeHolder = 0
		for n in self.Openl:
			++count 
		rowL = count/count 
		parent = self.Openl[self.Stat]
		self.Openl[self.Start + rowL + 1].parent = parent
		self.Openl[self.Start + rowL - 1].parent = parent
		self.Openl[self.Start - rowL].parent = parent
		self.Openl[self.Start - rowL + 1].parent = parent
		self.Openl[self.Start - rowL - 1].parent = parent
		self.Openl[self.Start + 1].parent = parent
		self.Openl[self.Start - 1].parent = parent
		
	def Gcost
		
		
	def closeL(self):
		return self.closeL
		
		
		
	
	