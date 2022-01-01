import collections
import operator
import os
import q1
import sys
import tabulate
import time

tabulate.PRESERVE_WHITESPACE = True


def print_stacks(passn, s1, s2, s3):
    os.system("clear")
    print("pass %d" % passn)
    s1lines = s1.aslines()
    s2lines = s2.aslines()
    s3lines = s3.aslines()
    assert len(s1lines) == len(s2lines) == len(s3lines)
    out = [None] * len(s1lines)
    for i in range(len(s1lines)):
        out[i] = [s1lines[i], s2lines[i], s3lines[i]]
    print(tabulate.tabulate(out, tablefmt="fancy_grid", stralign="center"))


# Solution from https://python-course.eu/applications-python/towers-of-hanoi.php
def hanoi(n, source, helper, target):
    print_stacks(n, s1, s2, s3)
    time.sleep(1)

    if n > 0:

        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.push(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)


def myhanoi(stacks, max_element):
    solved = False
    should_reverse = False
    passn = 0
    while not solved:
        moved = False

        lookinto = stacks
        if should_reverse:
            lookinto = list(reversed(stacks))
        else:
            if s3.empty():   # Hacky? to get the max element to continue to be pushed to the last stack.
                for s in [s for s in stacks if not s.empty()]:  # empty stacks.
                    if s.peek() == max_element:
                        s3.push(s.pop())
                        moved = True

        if not moved:
            for i, s in enumerate(lookinto):
                if s.empty():
                    continue
                element = s.peek()
                for other in lookinto[i:]:
                    if other != s and (other.empty() or other.peek() > element):
                        other.push(s.pop())
                        print("move to other")
                        moved = True
                        break
                if moved:
                    break
        if not moved:
            if should_reverse:
                should_reverse = False
            else:
                should_reverse = True

        passn += 1
        print_stacks(passn, s1, s2, s3)
        time.sleep(1)

        if s1.empty() and s2.empty():
            solved = True


if __name__ == "__main__":

    print("""\nQ4: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes wihch can slide onto any tower.
The puzzle starts with disks sorted in ascending order of size from top to bottom (i.e., each disk sits on top of an even larger one). You have the following constraints:
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto the next tower.
(3) A disk can only be placed on top of a larger disk.
Write a program to move the disks from the first tower to the last using stacks.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    s1 = q1.Stack(q1.UARRAY, q1.MAX_STACK_SIZE * 0, q1.MAX_STACK_SIZE)
    s2 = q1.Stack(q1.UARRAY, q1.MAX_STACK_SIZE * 1, q1.MAX_STACK_SIZE)
    s3 = q1.Stack(q1.UARRAY, q1.MAX_STACK_SIZE * 2, q1.MAX_STACK_SIZE)

    print("**** Recursive solution works for any number of disks:")
    time.sleep(2)

    s1_initial_elements = range(2, 10, 2)
    for i in reversed(s1_initial_elements):
        s1.push(i)

    print_stacks(-1, s1, s2, s3)
    time.sleep(1)

    hanoi(len(s1_initial_elements), s1, s2, s3)

    # ================================

    s1.clear()
    s2.clear()
    s3.clear()

    print("**** My solution works for 3 disks:")
    time.sleep(2)

    s1_initial_elements = range(2, 8, 2)
    for i in reversed(s1_initial_elements):
        s1.push(i)

    print(s1)

    print_stacks(-1, s1, s2, s3)
    time.sleep(1)

    stacks = [s1, s2, s3]
    max_element = s1_initial_elements[-1]
    myhanoi(stacks, max_element)

    sys.exit(0)
