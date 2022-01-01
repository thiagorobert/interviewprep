import common
import math
import sys


# I struggled with this, created implementation above first (misunderstanding BST) and the looked at
# https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/
def populateBST(input, current_depth = 0):
    if not input:
        return None
    index = math.floor(len(input) / 2)
    root = common.Node(current_depth, input[index])
    #print("L: input[:index] == %s" % input[:index])
    root.Left = populateBST(input[:index], current_depth + 1)
    #print("R: input[index + 1:] == %s" % input[index + 1:])
    root.Right = populateBST(input[index + 1:], current_depth + 1)
    return root


if __name__ == "__main__":

    print("""\nQ3: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    input = [*range(15)]
    print("input: %s" % input)

    depth = common.depth_for(len(input))
    print("need a binary tree with depth: %d\n" % depth)

    root = populateBST(input)

    with open("/tmp/tree.out", "w") as f:
        f.write(str(root))

    common.print_tree(depth, root)
    print("BST? ", common.checkBST(root))
