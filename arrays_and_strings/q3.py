import sys


if __name__ == "__main__":

    print("\nQ3: Given two strings, write a method to decide if one is a permutation of the other.\n\n")

    inputstrs = []

    if len(sys.argv) > 2:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)
    elif len(sys.argv) == 2:
        inputstrs.append(sys.argv[1])
    else:
        inputstrs = [("leolabs", "ballseo"), ("test", "tests"), ("dog", "god")]

    for input_tuple in inputstrs:
        assert len(input_tuple) == 2
        if sorted(input_tuple[0]) == sorted(input_tuple[1]):
            print("\nTRUE: %s is a permutation of %s\n" % (input_tuple[0], input_tuple[1]))
        else:
            print("\nFALSE: %s is NOT a permutation of %s\n" % (input_tuple[0], input_tuple[1]))

