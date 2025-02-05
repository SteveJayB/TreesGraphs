################################################
#             Stephen Bridgett                 #
#             Trees and Graphs                 #
################################################

class Node:
    def __init__(self, data):
        """Initialize a node with data and an empty list of children."""
        self.data = data
        self.children = []

    def get_data(self):
        """Return node data."""
        return self.data

    def set_data(self, new_data):
        """Update node data."""
        self.data = new_data

    def get_children(self):
        """Return list of children nodes."""
        return self.children

    def add_child(self, data):
        """Add a new child node with given data and return it."""
        new_node = Node(data)
        self.children.append(new_node)
        return new_node

    def print_node(self):
        """Recursively print node and its children."""
        print(self.data, end=' [ ')
        for child in self.children:
            child.print_node()
        print('] ', end='')

    def add_child_node(self, child_node):
        """Add an existing child node."""
        self.children.append(child_node)


class Tree:
    def __init__(self, data):
        """Initialize tree with root node."""
        self.root = Node(data)

    def get_root(self):
        """Return root node."""
        return self.root

    def insert(self, path, data):
        """Insert a node at a given path in the tree."""
        temp_node = self.root
        for index in path:
            if 0 <= index < len(temp_node.children):
                temp_node = temp_node.children[index]
            else:
                return  # Invalid path, do nothing
        temp_node.add_child(data)

    def print_tree_recursive(self, current_node):
        """Recursively print tree nodes."""
        print(current_node.get_data())
        for child in current_node.get_children():
            self.print_tree_recursive(child)

    def print_tree(self):
        """Print entire tree from the root."""
        self.print_tree_recursive(self.root)

    def search_tree(self, item):
        """Search for an item in the tree recursively."""
        def dfs(node):
            if node.get_data() == item:
                return True
            return any(dfs(child) for child in node.get_children())
        
        return dfs(self.root)


# Test Tree
print("\n------------------ Tree ------------------")
t = Tree(7)
t.insert([], 8)
t.insert([], 2)
t.insert([], 4)
t.insert([], 6)
t.insert([1], 9)
t.insert([1], 1)
t.insert([1, 0], 5)
t.print_tree()
print()


class Tree1:
    def __init__(self):
        """Initialize an empty tree."""
        self.root = None

    def set_root(self, data):
        """Set the root node with given data."""
        self.root = Node(data)
        return self.root

    def recursive_search(self, item, node=None):
        """Recursively search for an item in the tree."""
        if node is None:
            node = self.root
        if not node:
            return False
        if node.get_data() == item:
            return True
        return any(self.recursive_search(item, child) for child in node.get_children())

    def dfs(self, item):
        """Perform depth-first search (DFS) to find an item."""
        if not self.root:
            return False
        
        visited = set()
        stack = [self.root]

        while stack:
            node = stack.pop()
            print(node.get_data())
            if node.get_data() == item:
                return True
            
            visited.add(node)
            for child in node.get_children():
                if child not in visited:
                    stack.append(child)
        
        return False


# Test Tree1
def tree1_test():
    t = Tree1()
    n1 = t.set_root(1)
    n4 = n1.add_child(4)
    n12 = n1.add_child(12)
    n4.add_child(7)
    n4.add_child(8)
    n12.add_child(111)
    return t


class DGraph:
    def __init__(self):
        """Initialize an empty directed graph."""
        self.vertices = {}

    def make_vertex(self, node):
        """Add a vertex if it is a Node and not already present."""
        if isinstance(node, Node) and node.data not in self.vertices:
            self.vertices[node.data] = node
            return True
        return False

    def make_edge(self, v1, v2):
        """Create a directed edge between two existing vertices."""
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_child_node(self.vertices[v2])
            return True
        return False

    def print_graph(self):
        """Print the adjacency list representation of the graph."""
        for key in sorted(self.vertices.keys()):
            children = [child.get_data() for child in self.vertices[key].get_children()]
            print(f"{key}: {children}")


# Test Directed Graph
graph = DGraph()
first = Node('A')
graph.make_vertex(first)
for i in range(ord('A'), ord('K')):
    graph.make_vertex(Node(chr(i)))

edges = ['AB', 'AE', 'BK', 'BS', 'BY', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.make_edge(edge[0], edge[1])

print("------------- Directed Graph -------------")
graph.print_graph()
print()

##############################################################################################################
#   The worst-case running time of the search functions is O(n^2). This is because each function iterates    #
#   through the tree or graph and then compares values, which can result in quadratic complexity in some    #
#   cases. Optimizations such as better indexing structures can improve performance.                        #
##############################################################################################################
