import sys


if __name__ == "__main__":

    print("""\nQ5: Implement a mthod to perform basic string compression using the counts of
replaced characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string,
your method should return the original string.
You can assume the string has only upper and lower case letters (a-z).\n\n""")

    inputstrs = []

    if len(sys.argv) > 2:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)
    elif len(sys.argv) == 2:
        inputstrs.append(sys.argv[1])
    else:
        inputstrs = ["leolabs", "aabcccccaaa"]

    for inputstr in inputstrs:
        outstr = ""
        i = 0
        while i < len(inputstr):
            nsame = 1
            currc = inputstr[i]
            i += 1
            while i < len(inputstr) and inputstr[i] == currc:
                nsame += 1
                i += 1
            outstr += "%s%d" % (currc, nsame)
        if len(outstr) > len(inputstr):
            outstr = inputstr
        print("%s compressed: %s\n" % (inputstr, outstr))

