import collections
import random
import sys


if __name__ == "__main__":

    print("""\nQ6: There are 100 closed lockers in a hallway. A man begins by opening all 100 lockers.\n
Next, he closes every second locker. Then, on his third pass, he toggles every third locker (closes it if it is open or opens it if it is closed).\n
This proces continues for 100 passes, such that on each pass i, the man toggles every ith locker. After his 100th pass in the hallway, in which he toggles only locker #100, how many lockers are open?\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    lockers = ['O'] * 101
    lockers[0] = ''
    for npass in range(2, 101):
        for nlocker in range(1, 101):
            if nlocker % npass == 0:
                if lockers[nlocker] == 'O':
                    lockers[nlocker] = 'C'
                else:
                    lockers[nlocker] = 'O'
        print("".join(lockers))
    nopen = 0
    for i in range(1, 101):
        if lockers[i] == 'O':
            nopen += 1
    print("%d lockers are open" % nopen)
    print("".join(lockers))
