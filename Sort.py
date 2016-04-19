import Nodes
from Nodes import *



def LowestNode(na):
	n = Node()
	temp = 0
	currentValue = 0
	smallestValue = 0
	for sn in na:
		temp = na[currentValue + 1].x
		if sn.x < temp:
			smallestValue = sn.x
		++currentValue
	return smallestValue

def main():
	nodeList =[]
	n1 = Node(1,2)
	n2 = Node(3,4)
	n3 = Node(5,6)
	n4 = Node(7,8)
	n5 = Node(9,10)
	
	nodeList.append(n1)
	nodeList.append(n2)
	nodeList.append(n3)
	nodeList.append(n4)
	nodeList.append(n5)
	

	print(LowestNode(nodeList))
	
main()