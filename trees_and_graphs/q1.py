import common
import os
import random
import sys


# Constants.
FIXED = True
MAX_VALUE = 9
TREE_DEPTH = 5
BALANCED_THRESHOLD = 1
PROBABILITY_UNBALANCED_PERCENT = 25

# Globals.
fixed = 0


def get_value():
    if FIXED:
        global fixed
        fixed += 1
        return fixed
    else:
        return random.randint(0, MAX_VALUE)


def maybe_add_children(node, depth):
    out = []
    new_node = common.Node(i, get_value())
    node.Left = new_node
    out.append(new_node)
    if random.randint(1, 100) > PROBABILITY_UNBALANCED_PERCENT:
        new_node = common.Node(i, get_value())
        node.Right = new_node
        out.append(new_node)
    return out


def balanced(root, threshold):
    current = root
    lheight = 0
    while current.Left != None:
        lheight += 1
        current = current.Left
        if not (balanced(current, threshold)):
            return False

    current = root
    rheight = 0
    while current.Right != None:
        rheight += 1
        current = current.Right
        if not (balanced(current, threshold)):
            return False

    #print("V: %d | LH: %d | RH: %d" % (current.Value, lheight, rheight))
    return abs(lheight - rheight) <= threshold


if __name__ == "__main__":

    print("""\nQ1: Implement a function to check if a binary tree is balanced.
For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    root = common.Node(0, get_value())
    new_nodes = [root]

    n_nodes = len(new_nodes)
    for i in range(1, TREE_DEPTH):
        added_nodes = []
        for node in new_nodes:
            added_nodes.extend(maybe_add_children(node, i))
        new_nodes = added_nodes
        n_nodes += len(new_nodes)

    print("# nodes: %d\n" % n_nodes)

    with open("/tmp/tree.out", "w") as f:
        f.write(str(root))
    common.print_tree(TREE_DEPTH, root)

    if balanced(root, BALANCED_THRESHOLD):
        print("BALANCED TREE")
        sys.exit(0)
    else:
        print("UNBALANCED TREE")
        sys.exit(-1)
