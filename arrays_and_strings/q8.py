import sys


if __name__ == "__main__":

    print("""\nQ8: Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
E.g., "waterbottle" is a rotation of erbottlewat".\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    s1 = "erbottlewat"
    s2 = "waterbottle"

    if s2 in s1+s1:
        print("TRUE: '%s' is a rotation of '%s'" % (s2, s1))
    else:
        print("FALSE: '%s' is NOT a rotation of '%s'" % (s2, s1))
