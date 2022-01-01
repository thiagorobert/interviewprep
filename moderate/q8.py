import random
import sys


# This solutin is O(N^2).


VERBOSE = False


def mylog(entry, enable=VERBOSE):
    if enable:
        print(entry)


def largest_sum_and_sequence(seq):
    max_sum = -999
    out_seq = None
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            isum = sum(seq[i:j])
            mylog("i: %d\t| j: %d\t| seq[i:j]: %s\t| isum: %d" % (i, j, seq[i:j], isum))
            if isum > max_sum:
                max_sum = isum
                out_seq = seq[i:j]
    return max_sum, out_seq


if __name__ == "__main__":

    print("""\nQ8: You are given an array of integers (both positive and negative).\n
Find the contiguous sequence with the largest sum Eg.: for (2, -8, 3, -2, 4, -10) the output is 5, for sequence (3, -2, 4).\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    test_seq = [2, -8, 3, -2, 4, -10]
    out_sum, out_seq = largest_sum_and_sequence(test_seq)
    print("input: %s\nsum: %d\t| seq: %s\n\n" % (test_seq, out_sum, out_seq))

    for _ in range(1):
        size = random.randint(1, 10)
        input_seq = []
        for _ in range(size):
            input_seq.append(random.randint(-10, 10))
        print("input: %s" % (input_seq))
        out_sum, out_seq = largest_sum_and_sequence(input_seq)
        print("input: %s\nsum: %d\t| seq: %s\n" % (input_seq, out_sum, out_seq))
