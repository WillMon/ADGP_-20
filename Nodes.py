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

	def __init__(self, nl):
		self.NodeList = nl
		self.currentNode = Node()
	
	def sort(self):
		temp = []
		placeHolder = 0
		for n in self.NodeList:
			if 
			
		
	
	