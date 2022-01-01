import collections
import random
import sys

# This solutin is O(N^4).


MATRIX_SIZE = 20
VERBOSE = False
PROB_STAR = 85


def mylog(entry, enable=VERBOSE):
    if enable:
        print(entry)


def isSquare(start_row, start_column, size, matrix):
    mylog("isSquare? start_row: %d\t| start_column: %d\t| size: %d" % (start_row, start_column, size))
    for i in range(size):
        mylog("matrix[start_row][start_column + i]: %s" % matrix[start_row][start_column + i])
        if matrix[start_row][start_column + i] != "*":
            return False
        mylog("matrix[start_row + size - 1][start_column + i]: %s" % matrix[start_row + size - 1][start_column + i])
        if matrix[start_row + size - 1][start_column + i] != "*":
            return False
    for i in range(1, size - 1):
        mylog("matrix[start_row + i][start_column]: %s" % matrix[start_row + i][start_column])
        if matrix[start_row + i][start_column] != "*":
            return False
        mylog("matrix[start_row + i][start_column + size - 1]: %s" % matrix[start_row + i][start_column + size - 1])
        if matrix[start_row + i][start_column + size - 1] != "*":
            return False
    return True


if __name__ == "__main__":

    print("""\nQ11: Imagine you have a square matrix, where each cell (pixel) is either black or white.\n
Design an algorithm to find the maximum subsquare such that all four BORDERS are filled with black pixels.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    matrix = [None] * MATRIX_SIZE
    for i in range(MATRIX_SIZE):
        line = []
        for _ in range(MATRIX_SIZE):
            line.append("*" if random.randint(0, 100) < PROB_STAR else " ")
        matrix[i] = line

    for square_size in reversed(range(2, MATRIX_SIZE + 1)):
        mylog("searching for square size: %d" % square_size)
        count = MATRIX_SIZE - square_size + 1
        for start_row in range(count):
            for start_column in range(count):
                if isSquare(start_row, start_column, square_size, matrix):
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

                        print("%s               %s" % (" ".join(matrix[i]), square_line))

                    sys.exit(1)

    print("NOT FOUND!")
    for i in range(MATRIX_SIZE):
        print(" ".join(matrix[i]))
