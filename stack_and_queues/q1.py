import collections
import operator
import sys


UARRAY = [None] * 12
N_STACKS = 3
MAX_STACK_SIZE = int(len(UARRAY) / N_STACKS)


class Stack:
    def __init__(self, uarray, init_index, max_size):
        self.uarray = uarray
        self.size = 0
        self.init_index = init_index
        self.index = self.init_index
        self.max_size = max_size

    def push(self, element):
        if self.size + 1 > self.max_size:
            raise IndexError("can't push to full stack (max_size == %d)!" % self.max_size)
        self.uarray[self.index] = element
        self.index += 1
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("can't pop from empty stack!")
        self.index -= 1
        out = self.uarray[self.index]
        self.size -= 1
        return out

    def peek(self):
        if self.size == 0:
            raise IndexError("can't peek empty stack!")
        return self.uarray[self.index - 1]

    def clear(self):
        self.size = 0
        self.index = self.init_index

    def empty(self):
        return self.size == 0

    def print_csv(self):
        return ",".join([str(i) for i in self.uarray[self.init_index:self.index]])

    def aslines(self):
        out = []
        for element in self.uarray[self.init_index:self.index]:
            out.insert(0, "*" * element)
        for _ in range(len(out), self.max_size):
            out.insert(0, " " * 8)
        return out

    def __str__(self):
        return "\n".join(self.aslines())


if __name__ == "__main__":

    print("""\nQ1: Describe how you could use a single array to implement three stacks.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    s1 = Stack(UARRAY, MAX_STACK_SIZE * 0, MAX_STACK_SIZE)
    s2 = Stack(UARRAY, MAX_STACK_SIZE * 1, MAX_STACK_SIZE)
    s3 = Stack(UARRAY, MAX_STACK_SIZE * 2, MAX_STACK_SIZE)

    for i in range(MAX_STACK_SIZE):
        s1.push(i)
        s2.push(i*3)
        s3.push(i*9)

    print(s1)
    print(s2)
    print(s3)

    try:
        s1.push(5)
    except IndexError as e:
        print("s1 push error: %s" % e)

    for i in range(MAX_STACK_SIZE):
        print(s1.pop())
        print(s2.pop())
        print(s3.pop())

    print("s1 size: %d" % s1.size)

    try:
        s1.pop()
    except IndexError as e:
        print("s1 pop error: %s" % e)
