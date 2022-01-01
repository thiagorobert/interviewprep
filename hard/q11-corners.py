import collections
import random
import sys


MATRIX_SIZE = 20
VERBOSE = False
PROB_STAR = 30


def mylog(entry, enable=VERBOSE):
    if enable:
        print(entry)


if __name__ == "__main__":

    print("""\nQ11: Imagine you have a square matrix, where each cell (pixel) is either black or white.\n
Design an algorithm to find the maximum subsquare such that all four CORNERS are filled with black pixels.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    matrix = [None] * MATRIX_SIZE
    for i in range(MATRIX_SIZE):
        line = []
        for _ in range(MATRIX_SIZE):
            line.append("*" if random.randint(0, 100) < PROB_STAR else "^")
        matrix[i] = line

    losets = collections.defaultdict(set)
    for i in range(len(matrix)):
        mylog(" ".join(matrix[i]))
        for j, p in enumerate(matrix[i]):
            if p == "*":
                losets[i].add(j)

    matches = []
    for i in range(len(losets)):
        for j in range(i + 1, len(losets)):
            isect = losets[i].intersection(losets[j])
            mylog("i: %d\tj: %d\tisec: %s" % (i, j, isect))
            if len(isect) > 2:
                l = list(isect)
                l.sort()
                matches.append((i, j, l))

    if not matches:
        for i in range(len(matrix)):
            print(" ".join(matrix[i]))
        print("No subsquares!")
        sys.exit(-1)

    max_area = -1
    max_match = None
    for m in matches:
        area = (m[1] - m[0]) * len(m[2])
        if area > max_area:
            max_area = area
            max_match = m
        mylog("area: %s\tmax_area: %s" % (area, max_area))

    print("Max subsquare: start_row: %s\t| end_row: %s\t| overlapping pixels: %s" % (max_match[0], max_match[1], max_match[2]))

    print()

    for i in range(len(matrix)):
        square_line = ""
        if i >= max_match[0] and i <= max_match[1]:
            for p in range(len(matrix[i])):
                if p in max_match[2]:
                    square_line += matrix[i][p] + " "
                else:
                    square_line += ". "
        else:
            square_line = ". " * len(matrix[i])

        print("%s               %s" % (" ".join(matrix[i]), square_line))
