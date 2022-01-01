import common
import collections
import sys


def DFS(root_node, graph, visited=None):
    if visited == None:
        visited = []
    graph.visit(root_node)
    visited.append(root_node)
    for adjacent in g.graph[root_node]:
        if adjacent not in visited:
            DFS(adjacent, graph, visited)
    return visited


def BFS(root_node, graph):
    visited = set()

    graph.visit(root_node)
    visited.add(root_node)

    toprocess = collections.deque()
    toprocess.appendleft(root_node)

    while toprocess:
        n = toprocess.pop()
        for node in graph.graph[n]:
            if node not in visited:
                graph.visit(node)
                visited.add(node)
                toprocess.appendleft(node)
    return visited


if __name__ == "__main__":

    print("""\nQ1: Depth First Search (DFS) and Breadth First Search (BFS) of a graph.\n\n""")


    if len(sys.argv) > 1:
        print("usage: python3 %s <string>" % sys.argv[0])
        sys.exit(-1)

    #g = common.get_random_graph(min_nodes=2, max_nodes=4, connected_probability=99)
    g = common.Graph()
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    print(g.graph)
    print("\n\n# nodes: %d\t| connected: %s" % (len(g.nodes()), g.connected()))
    #search_root = g.nodes()[0]
    search_root = 2

    print("\n\n***************** DFS!!\n")

    visited = DFS(search_root, g)
    print()

    print("sorted(g.nodes()):\t%s" % sorted(g.nodes()))
    print("sorted(visited):\t\t%s" % sorted(visited))
    if sorted(g.nodes()) != sorted(visited):
        print("\n\n\n\nERRORR!")
        sys.exit(-1)

    print("\n\n***************** BFS!!\n")

    visited = BFS(search_root, g)
    print()

    print("sorted(g.nodes()):\t%s" % sorted(g.nodes()))
    print("sorted(visited):\t\t%s" % sorted(visited))
    if sorted(g.nodes()) != sorted(visited):
        print("\n\n\n\nERRORR!")
        sys.exit(-1)
