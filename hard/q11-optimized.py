import collections
import random
import sys

# This solutin is O(N^3).


MATRIX_SIZE = 9
VERBOSE = False
PROB_STAR = 85


def mylog(entry, enable=VERBOSE):
    if enable:
        print(entry)


class Metadata(object):
    def __init__(self):
        self.zright = 0
        self.zbelow = 0
    def __str__(self):
        return "%d,%d" % (self.zright, self.zbelow)


def isSquare(start_row, start_column, size, pmatrix):
    mylog("isSquare? start_row: %d\t| start_column: %d\t| size: %d" % (start_row, start_column, size))
    topLeft = pmatrix[start_row][start_column]
    topRight = pmatrix[start_row][start_column + size - 1]
    bottomLeft = pmatrix[start_row + size - 1][start_column]

    return topLeft.zright >= size and topLeft.zbelow >= size and topRight.zbelow >= size and bottomLeft.zright >= size


if __name__ == "__main__":

    print("""\nQ11: Imagine you have a square matrix, where each cell (pixel) is either black or white.\n
Design an algorithm to find the maximum subsquare such that all four BORDERS are filled with black pixels.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    matrix = [None] * MATRIX_SIZE
    pmatrix = [None] * MATRIX_SIZE
    for i in range(MATRIX_SIZE):
        line = []
        for _ in range(MATRIX_SIZE):
            line.append("*" if random.randint(0, 100) < PROB_STAR else " ")
        matrix[i] = line

        line = []
        for _ in range(MATRIX_SIZE):
            line.append(Metadata())
        pmatrix[i] = line

    for r in reversed(range(MATRIX_SIZE)):
        for c in reversed(range(MATRIX_SIZE)):
            if matrix[r][c] == "*":
                pmatrix[r][c].zright += 1
                pmatrix[r][c].zbelow += 1
                if c + 1 < MATRIX_SIZE:
                    pmatrix[r][c].zright += pmatrix[r][c + 1].zright
                if r + 1 < MATRIX_SIZE:
                    pmatrix[r][c].zbelow += pmatrix[r + 1][c].zbelow


    for square_size in reversed(range(2, MATRIX_SIZE + 1)):
        mylog("searching for square size: %d" % square_size)
        count = MATRIX_SIZE - square_size + 1
        for start_row in range(count):
            for start_column in range(count):
                if isSquare(start_row, start_column, square_size, pmatrix):
                    print("FOUND SQUARE: start_row: %d\t| start_column: %d\t| size: %d\t" % (start_row, start_column, square_size))

                    # Print original matrix and the square just identified.
                    for i in range(MATRIX_SIZE):
                        square_line = ""
                        if i >= start_row and i < start_row + square_size:
                            for p in range(len(matrix[i])):
                                if p >= start_column and p < start_column + square_size:
                                    square_line += matrix[i][p] + " "
                                else:
                                    square_line += "  "
                        else:
                            square_line = "  " * len(matrix[i])

                        print("%s               %s               %s" % (" ".join(matrix[i]), " ".join([str(e) for e in pmatrix[i]]), square_line))

                    sys.exit(1)

    print("NOT FOUND!")
    for i in range(MATRIX_SIZE):
        print(" ".join(matrix[i]))
