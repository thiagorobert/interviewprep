import math
import random
import string
import sys


VERBOSE = False


def mylog(entry, enable=VERBOSE):
    if enable:
        print(entry)


def find_permutations(input_str):
    if len(input_str) <= 0:
        raise Exception("invalid input")
    if len(input_str) == 1:
        return [input_str,]
    last_char = input_str[-1:]
    permutations = find_permutations(input_str[:-1])
    out = []
    for p in permutations:
        plist = list(p)
        for i in range(len(plist)):
            plist_copy = plist[:]
            plist_copy.insert(i, last_char)
            out.append("".join(plist_copy))
        out.append(p + last_char)
    return out


if __name__ == "__main__":

    print("""\nQ: Print all permutations of a string. For simplicity, assume all characters are unique.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    unique_characters = list(string.ascii_lowercase)[:10]

    for i in range(len(unique_characters)):
        input_str = "".join(unique_characters[i:])
        permutations = find_permutations(input_str)
        if len(permutations) != math.factorial(len(input_str)):
            print("ERROR: expected %d permutations for input '%s', got %d" % (math.factorial(len(input_str), input_str, len(permutations))))
            sys.exit(-1)
        print(permutations)
        print("%d permutations for input '%s'\n\n" % (len(permutations), input_str))
