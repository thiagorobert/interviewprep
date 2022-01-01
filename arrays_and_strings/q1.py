import sys

def all_unique(inputstr):
    sorted_inputstr = sorted(inputstr)
    for i, c in enumerate(sorted_inputstr[1:]):
        if c == sorted_inputstr[i]:
            print("FALSE: repeated character: %s" % c)
            return False

    print("TRUE: all unique characters in : %s" % inputstr)
    return True


if __name__ == "__main__":

    print("\nQ1: Implement an algo to determine if a string has all unique characters.\n\n")

    inputstrs = []

    if len(sys.argv) > 2:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)
    elif len(sys.argv) == 2:
        inputstrs.append(sys.argv[1])
    else:
        inputstrs = ["leolabs", "test", "dog"]

    for inputstr in inputstrs:
       all_unique(inputstr)
