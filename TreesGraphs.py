################################################
#             Stephen Bridgett                 #
#             Trees and Graphs                 #
################################################

class Node:
    def __init__(self, idata):
        self.data = idata
        self.children = []

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getChildren(self):
        return self.children

    def addChild(self, idata):
        newNode = Node(idata)
        self.children.append(newNode)
        return newNode

    def printNode(self):
        print(self.data, end = ' ')
        print("[", end = ' ')
        for child in self.children:
            child.printNode()
        print("]", end = ' ')

    def addChildNode(self, childnode):
        self.children.append(childnode)

class Tree:
    def __init__(self, data):
        node = Node(data)
        self.root = node

    def getRoot(self):
        return self.root

    def insert(self, data, node):
        tempNode = self.root
        for i in data:
            tempNode = tempNode.getChildren()[i]
        tempNode.addChild(node)

    def printTreeRecursive(self, currentNode):
        if currentNode.getChildren() == []:
            print(currentNode.getData())
        else:
            print(currentNode.getData())
            for i in range(len(currentNode.getChildren())):
                self.printTreeRecursive(currentNode.getChildren()[i])
                
    def printTree(self):
        tempNode = self.getRoot()
        self.printTreeRecursive(tempNode)

    def searchTree(self, item):
        for node in self.children:
            n = node.find(item)
            if n:
                return True
        return False    
        
#test
print()
print("------------------ Tree ------------------")
t = Tree(7)
t.insert([],8)
t.insert([],2)
t.insert([],4)
t.insert([],6)
t.insert([1], 9)
t.insert([1],1)
t.insert([1, 0],5)
t.printTree()
print()


class Tree1:
    def __init__(self):
        self.root = None

    def setRoot(self, idata):
        newnode = Node(idata)
        self.root = newnode
        return newnode

    def recursivesearch(self, item, node = None):
        if node == None:
            node = self.root
        if node == None:
            return False
        if node.getData() == item:
            return True
        else:
            for child in node.getChildren():
                if self.recursivesearch(item, child) == True:
                    return True
            return False
        
    def dfs(self, item):
        if self.root == None:
            return False
        node = self.root
        print(node.getData())
        if node.getData() == item:
            return True
        visited[node] = 1
        stack = []
        for child in node.getChildren():
            if child not in visited:
                stack.append(child)
        while len(stack) > 0:
            node = stack.pop()
            print(node.getData())
            if node.getData() == item:
                return True
            else:
                visited[node] = 1
                for child in node.getChildren():
                    if child not in visited:
                        stack.append(child)
        return False       

                
def Tree1Test():
    t = Tree1()
    n1 = t.setRoot(1)
    n4 = n1.addChild(4)
    n12 = n1.addChild(12)
    n7 = n4.addChild(7)
    n8 = n4.addChild(8)
    n111 = n12.addChild(111)
    return t


        
class dGraph:
    def __init__(self):
        self.vertices = {}

    def makeVertex(self, vertex):
        if isinstance(vertex, Node) and vertex.data not in self.vertices:
            self.vertices[vertex.data] = vertex
            return True
        else:
            return False

    def makeEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices: 
            self.vertices[v1].addChildNode(v2)            
            self.vertices[v2].addChildNode(v1)           
            return True
        else:
            return False
        
    def searchGraph(self, graph, item):
        for i in graph:
            if graph[i] == item:
                return True
            else:
                return False
     
    def printGraph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].children))

#test
graph = dGraph()
first = Node('A')
graph.makeVertex(first)
graph.makeVertex(Node('B'))
for i in range(ord('A'), ord('K')):
	graph.makeVertex(Node(chr(i)))

edges = ['AB', 'AE', 'BK', 'BS', 'BY', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	graph.makeEdge(edge[:1], edge[1:])
	
print("------------- Directed Graph -------------")
graph.printGraph()
print()

##############################################################################################################
#   The worst case running time of the above search functions would be O(n^2). This is known because each    #                 
#   function first runs through either the directed graph or the tree in a loop. After that, the item is     #
#   compared to the data in the tree or directed graph to see if that item actually exists.                  #
##############################################################################################################
