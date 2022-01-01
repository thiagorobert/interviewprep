import collections
import sys


# This is incomplete.


class TrieNode(object):
    def __init__(self, depth, value):
        self.Children = []
        self.Value = value
        self.depth = depth

    def __str__(self):
        identation = "\t" * self.depth
        out = "\n%s%s"  % (identation, self.Value)
        for c in self.Children:
            out += "\n%s%s" % (identation, str(c))
        return out


if __name__ == "__main__":

    print("""\nAdd a set of words to a trie.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)


    root = TrieNode(0, "*")
    words = {
        "a": root,
        "lie": root,
        "many": root,
        "my": root,
        "lyme": root,
    }

    max_len = max([len(w) for w in words])
    for i in range(max_len):
        new_nodes = []
        for w in words.keys():
            if i < len(w):
                character = w[i]
                if character not in [n.Value for n in new_nodes]:
                    nr = TrieNode(i + 1, character)
                    words[w].Children.append(nr)
                    words[w] = nr
                    new_nodes.append(nr)

    print(root)
