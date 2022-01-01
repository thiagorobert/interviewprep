import collections
import operator
import sys


if __name__ == "__main__":

    print("""\nPlaying with deque, a generalization of stacks and queues (which can be seen as a circular buffer too, if 'maxlen' is used).\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    #    deque = collections.deque(maxlen=4)
    deque = collections.deque(maxlen=None)
    deque.append(9)
    deque.appendleft(8)
    print(deque)
    deque.appendleft(7)
    deque.appendleft(6)
    deque.appendleft(5)
    print(deque)

    deque += collections.deque(range(3))
    print(deque)

    deque *= 2
    print(deque)

    deque.rotate(-1)
    print(deque)

    c = collections.Counter('gallahad')
    print(c)
    print(list(c.elements()))
    print(c.most_common(1))
    #print(c.total()) - python 3.10
