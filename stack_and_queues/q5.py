import q1
import random
import sys


UARRAY = [None] * 20
N_STACKS = 2
MAX_STACK_SIZE = int(len(UARRAY) / N_STACKS)


class Queue(object):
    def __init__(self):
        self.s1 = q1.Stack(UARRAY, MAX_STACK_SIZE * 0, MAX_STACK_SIZE)
        self.s2 = q1.Stack(UARRAY, MAX_STACK_SIZE * 1, MAX_STACK_SIZE)

    def add(self, element):
        if self.s1.size == self.s1.max_size:
            raise IndexError("can't add to full queue")
        self.s1.push(element)

    def remove(self):
        if self.s1.size == 0:
            raise IndexError("can't remove from empty queue")
        for _ in range(self.s1.size - 1):
            self.s2.push(self.s1.pop())
        out = self.s1.pop()
        while not self.s2.empty():
            self.s1.push(self.s2.pop())
        return out

    def empty(self):
        return self.s1.empty()

    def __str__(self):
        return ",".join([str(i) for i in self.s1.uarray[self.s1.init_index:self.s1.index]])


if __name__ == "__main__":

    print("""\nQ5: Implement a MyQueue class which implements a queue using two stacks.\n\n""")

    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    q = Queue()
    for i in range(MAX_STACK_SIZE):
        q.add(random.randint(1, 10))
    print("\nInitial queue:\n%s" % q)

    while not q.empty():
        print(q.remove())

