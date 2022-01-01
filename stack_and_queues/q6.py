import q1
import os
import random
import sys
import tabulate
import time


UARRAY = [None] * 20
N_STACKS = 2
MAX_STACK_SIZE = int(len(UARRAY) / N_STACKS)


def print_stacks(passn, s1, s2):
    os.system("clear")
    print("pass %d" % passn)
    s1lines = s1.aslines()
    s2lines = s2.aslines()
    assert len(s1lines) == len(s2lines)
    out = [None] * len(s1lines)
    for i in range(len(s1lines)):
        out[i] = [s1lines[i], s2lines[i]]
    print(tabulate.tabulate(out, tablefmt="fancy_grid", stralign="center"))
    time.sleep(1)


def sort_ascending(s1, s2, n_to_look):
    if n_to_look == 0:
        return
    lower_element = 999
    for i in range(n_to_look):
        e = s1.pop()
        if e <= lower_element:
            if lower_element != 999:
                s2.push(lower_element)
            lower_element = e
        else:
            s2.push(e)
    s1.push(lower_element)
    print_stacks(n_to_look, s1, s2)
    while not s2.empty():
        s1.push(s2.pop())
    sort_ascending(s1, s2, n_to_look - 1)


if __name__ == "__main__":

    print("""\nQ6: Write a program to sort a stack in ascending order (with biggest items on top).
You may use at most one additional stack to hold items, but you man not copy the elements into any other data structure (such as an array).
The stack supports the following operations: push, poo, peek, and isEmpty.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    s1 = q1.Stack(UARRAY, MAX_STACK_SIZE * 0, MAX_STACK_SIZE)
    s2 = q1.Stack(UARRAY, MAX_STACK_SIZE * 1, MAX_STACK_SIZE)

    for i in range(MAX_STACK_SIZE):
        s1.push(random.randint(1, 10))

    print_stacks(999, s1, s2)
    time.sleep(1)
    print("\nInitial stack:\n%s" % s1)

    sort_ascending(s1, s2, s1.size)

    print("\n\nSorted stack (biggest on top):\n%s" % s1)
