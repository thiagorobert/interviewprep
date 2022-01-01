import collections
import math
import random
import tabulate


tabulate.PRESERVE_WHITESPACE = True
SHOW_TABLE_FRAME = False


class Node(object):
    def __init__(self, depth, value):
        self.Right = None
        self.Left = None
        self.Value = value
        self.depth = depth

    def __str__(self):
        identation = "\t" * self.depth
        identation += "%d: " % self.depth
        out = "\n%sValue: %s"  % (identation, self.Value)
        out += "\n%sLeft: %s" % (identation, self.Left)
        out += "\n%sRight: %s" % (identation, self.Right)
        return out


def max_nodes_for(depth):
    # I struggled a bit to get to this, had to rely on
    # https://www.geeksforgeeks.org/relationship-number-nodes-height-binary-tree/
    out = 1
    for i in range(1, depth):
        out += pow(2, i)
    return out


def depth_for(n_nodes):
    cumulative_nodes = 0
    for i in range(100):
        cumulative_nodes += pow(2, i)
        if cumulative_nodes >= n_nodes:
            return i + 1
    return -1


def to_table(max_nodes, root, row, col, out):
    if row >= depth_for(max_nodes):
        return
    if root == None:
        out[row][col] = " "
        return

    out[row][col] = str(root.Value)
    # It took me a long time to get the the solution here. I tried a couple
    # different things:
    #  ** works for TREE_DEPTH <= 3
    #    offset = (TREE_DEPTH - (row + 1))
    #  ** works for TREE_DEPTH == 4
    #    offset = math.floor(TREE_DEPTH / (row + 1))
    # ultimately, what I needed to do was divide the row length by the
    # number of elements seen so far.
    #print("val: %d | row: %d | col: %d" % (root.Value, row, col))
    col_offset = math.ceil(max_nodes / pow(2, (row + 2)))
    #print("row: %d | offset: %d" % (row + 1, offset))
    to_table(max_nodes, root.Left, row + 1, col - col_offset, out)
    to_table(max_nodes, root.Right, row + 1, col + col_offset, out)


def print_tree(depth, root):
    max_nodes = max_nodes_for(depth)
    out = [None] * depth
    for i in range(depth):
        out[i] = [None] * max_nodes

    col = math.floor(max_nodes / 2)
    to_table(max_nodes, root, 0, col, out)
    tablefmt = "fancy_grid" if SHOW_TABLE_FRAME else "plain"
    headers = [i for i in range(max_nodes)] if SHOW_TABLE_FRAME else []
    print(tabulate.tabulate(out, headers=headers, tablefmt=tablefmt, stralign="center"))


# From https://www.geeksforgeeks.org/check-if-a-binary-tree-is-bst-simple-and-efficient-approach/
prev = -math.inf
def checkBST(root):
    """
    Function to check if Binary Tree is
    a Binary Search Tree
    :param root: current root node
    :return: Boolean value
    """
    # traverse the tree in inorder
    # fashion and update the prev node
    global prev

    if root:
        if not checkBST(root.Left):
            return False

        # Handles same valued nodes
        if root.Value < prev:
            print("root.Value: %d | prev: %d" % (root.Value, prev))
            return False

        # Set value of prev to current node
        prev = root.Value

        return checkBST(root.Right)
    return True


class Graph(object):
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def nodes(self):
        return list(self.graph.keys())

    def addNode(self, value):
        self.graph[value] = []

    def addEdge(self, snode, dnode):
        self.graph[snode].append(dnode)

    def visit(self, node_value):
        if node_value not in self.nodes():
            raise Exception("Node %d not in graph" % node_value)
        print(node_value, end=" ")

    def connected(self):
        connected_nodes = []
        for n in self.nodes():
            for on in self.nodes():
                if n != on and n not in connected_nodes:
                    if n in self.graph[on]:
                        connected_nodes.append(n)
        print("sorted(self.nodes()):\t\t%s" % sorted(self.nodes()))
        print("sorted(connected_nodes):\t\t%s" % sorted(connected_nodes))
        return sorted(self.nodes()) == sorted(connected_nodes)


def get_random_graph(min_nodes=2, max_nodes=8, connected_probability=75):
    g = Graph()
    nnodes = random.randint(min_nodes, max_nodes)
    unique_node_values = []
    for _ in range(nnodes):
        node_value = random.randint(1, 20)
        while node_value in unique_node_values:
            node_value = random.randint(1, 20)
        unique_node_values.append(node_value)
        g.addNode(node_value)

    for n in g.nodes():
        for on in g.nodes():
            if random.randint(0, 100) < connected_probability:
                g.addEdge(n, on)

    return g
