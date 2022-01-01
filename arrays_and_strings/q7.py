import sys


TEST_MATRIX = """
1234
1204
0234
"""

if __name__ == "__main__":

    print("""\nQ7: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)


    input_lines = TEST_MATRIX.splitlines()
    max_len = max([len(r) for r in input_lines])

    matrix = []
    for l in input_lines:
        r = [int(e) for e in l]
        if r:
            matrix.append(r)

    print(matrix)

    rows_to_0 = []
    columns_to_0 = []

    for ri, row in enumerate(matrix):
        for ci in range(len(row)):
            if matrix[ri][ci] == 0:
                rows_to_0.append(ri)
                columns_to_0.append(ci)

    for ri, row in enumerate(matrix):
        for ci in range(len(row)):
            if ri in rows_to_0 or ci in columns_to_0:
                matrix[ri][ci] = 0


    print(matrix)

