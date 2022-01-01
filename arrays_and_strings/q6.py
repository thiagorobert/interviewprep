import sys


ART = """
                                    ___,,___
                                ,d8888888888b,_
                            _,d889'        8888b,
                        _,d8888'          8888888b,
                    _,d8889'           888888888888b,_
                _,d8889'             888888889'688888, /b
            _,d8889'               88888889'     `6888d 6,_
         ,d88886'              _d888889'           ,8d  b888b,  d\\
       ,d889'888,             d8889'               8d   9888888Y  )
     ,d889'   `88,          ,d88'                 d8    `,88aa88 9
    d889'      `88,        ,88'                   `8b     )88a88'
   d88'         `88       ,88                   88 `8b,_ d888888
  d89            88,      88                  d888b  `88`_  8888
  88             88b      88                 d888888 8: (6`) 88')
  88             8888b,   88                d888aaa8888, `   'Y'
  88b          ,888888888888                 `d88aa `88888b ,d8
  `88b       ,88886 `88888888                 d88a  d8a88` `8/
   `q8b    ,88'`888  `888'"`88          d8b  d8888,` 88/ 9)_6
     88  ,88"   `88  88p    `88        d88888888888bd8( Z~/
     88b 8p      88 68'      `88      88888888' `688889`
     `88 8        `8 8,       `88    888 `8888,   `qp'
       8 8,        `q 8b       `88  88"    `888b
       q8 8b        "888        `8888'
        "888                     `q88b
                                  "888'"""


TEST_ART = """
  ****
  \  +
  \  +
  ====
"""

def rotate90(matrix):
    max_len = len(matrix[0])
    out = []
    # rotate
    for _ in range(max_len):
        out.append([])

    out_i = 0
    for i in reversed(range(max_len)):
        for mr in matrix:
            #out[out_i].insert(0, mr[i])
            out[out_i].append(mr[i])
        out_i += 1
    return out


if __name__ == "__main__":

    print("""\nQ6: Given an image represented by an NxN matrix, where each pixel in the image is
4 bytes, write a method to rotate the image by 90 degrees.  Can you do this in place?\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    art_lines = ART.splitlines()
    max_len = max([len(r) for r in art_lines])

    matrix = []
    for l in art_lines:
        r = list(l)
        # fill in
        for _ in range(len(r), max_len):
            r.append(' ')
        matrix.append(r)

    print(matrix)

    for l in matrix:
        print("".join(l))

    rotated90 = rotate90(matrix)
    for l in rotated90:
        print("".join(l))

    rotated180 = rotate90(rotated90)
    for l in rotated180:
        print("".join(l))

    rotated270 = rotate90(rotated180)
    for l in rotated270:
        print("".join(l))

    rotated360 = rotate90(rotated270)
    for l in rotated360:
        print("".join(l))
