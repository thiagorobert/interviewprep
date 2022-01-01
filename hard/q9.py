import sys
import random
import statistics


VERBOSE = False


def mylog(entry, enable=VERBOSE):
    if enable:
        print(entry)


class MedianTracker(object):
    def __init__(self):
        self.seen = []
        self.median = None
        self.median_high = None
        self.median_low = None
        self.below = []
        self.above = []

    def Process(self, value):
        mylog("\nvalue: %d" % value)
        self.seen.append(value)
        if self.median == None:
            self.median = value
            self.median_low = value
            self.median_high = value
            self.below.append(value)
        else:
            if len(self.below) == len(self.above):
                if value > self.above[0]:
                    self.below.insert(0, self.above.pop(0))
                    self.above.append(value)
                    self.above.sort()
                else:
                    self.below.append(value)
                    self.below.sort(reverse=True)
            else:
                if value < self.below[0]:
                    self.above.insert(0, self.below.pop(0))
                    self.below.append(value)
                    self.below.sort(reverse=True)
                else:
                    self.above.append(value)
                    self.above.sort()

            if len(self.below) > len(self.above):
                self.median = self.below[0]
                self.median_low = self.below[0]
                self.median_high = self.below[0]
            else:
                self.median = (self.above[0] + self.below[0]) / 2
                self.median_low = self.below[0]
                self.median_high = self.above[0]

        mylog(self)


    def __str__(self):
        out = "CALCULATED low: %s\t| median: %s\t| high: %s" % (
            self.median_low,
            self.median,
            self.median_high)
        if VERBOSE:
            out += "\t| below: %s\t| above: %s\t" % (
                self.below,
                self.above)
            out += "\n"
            out += self.Verify()
        return out

    def Verify(self):
        return "CONFIRMING low: %s\t| median: %s\t| high: %s" % (
            statistics.median_low(self.seen),
            statistics.median(self.seen),
            statistics.median_high(self.seen))


if __name__ == "__main__":

    print("""\nQ9: Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    # validate logic:
    for _ in range(10000):
        t = MedianTracker()
        for i in range(random.randint(1, 100)):
            t.Process(random.randint(0, 100))
        if not t.median_low == statistics.median_low(t.seen):
            print("ERROR t.median_low: %s\t| statistics.median_low(t.seen): %s\t|%s" % (t.median_low, statistics.median_low(t.seen), t.seen))
            sys.exit(-1)
        if not t.median == statistics.median(t.seen):
            print("ERROR t.median: %s\t| statistics.median(t.seen): %s\t|%s" % (t.median, statistics.median(t.seen), t.seen))
            sys.exit(-1)
        if not  t.median_high == statistics.median_high(t.seen):
            print("ERROR t.median_high: %s\t| statistics.median_high(t.seen): %s\t|%s" % (t.median_high, statistics.median_high(t.seen), t.seen))
            sys.exit(-1)


    # illustrate logic:

    t = MedianTracker()
    for _ in range(4):
        t.Process(random.randint(0, 10))

    print("\n\nvalues:\t\t%s" % t.seen)
    print("sorted(values):\t%s" % sorted(t.seen))
    print()
    print(t)
    print()
    print(t.Verify())
