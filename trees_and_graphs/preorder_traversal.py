import common
import math
import sys


# From: https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
def preOrder(node):
    if not node:
        return

    print(node.Value)
    preOrder(node.Left)
    preOrder(node.Right)


index = 1
def solve(root, input, current_depth, max_depth):
    #print("root.Value: %d" % (root.Value))
    global index
    if current_depth >= max_depth:
        #print("current_depth: %d | max_depth: %d" % (current_depth, max_depth))
        return
    if root.Left == None:
        if index >= len(input):
            #print("index: %d | len(input): %d" % (index, len(input)))
            return
        root.Left = common.Node(current_depth, input[index])
        index += 1
        solve(root.Left, input, current_depth + 1, max_depth)
    if root.Right == None:
        if index >= len(input):
            #print("index: %d | len(input): %d" % (index, len(input)))
            return
        root.Right = common.Node(current_depth, input[index])
        index += 1
        solve(root.Right, input, current_depth + 1, max_depth)


def better_solve(input, current_depth = 0):
    if not input:
        return None
    #print("input: %s" % input)
    mid_index = math.floor(len(input) / 2)
    root = common.Node(current_depth, input[0])

    #print("L: input[1:mid_index] == %s" % input[1:mid_index + 1])
    root.Left = better_solve(input[1:mid_index + 1], current_depth + 1)
    #print("R: input[mid_index + 1:] == %s" % input[mid_index + 1:])
    root.Right = better_solve(input[mid_index + 1:], current_depth + 1)
    return root


if __name__ == "__main__":

    print("""\nWrite a function to add elements of a sorted array in to a balanced binary tree so pre-order traversal of the tree maintains the order.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    input = [*range(15)]
    print("input: %s" % input)

    depth = common.depth_for(len(input))
    print("need a binary tree with depth: %d\n" % depth)

    root = common.Node(0, input[0])
    solve(root, input, 1, depth)
    common.print_tree(depth, root)
    print()
    #preOrder(root)


    root = better_solve(input)
    common.print_tree(depth, root)
    print()
    preOrder(root)
