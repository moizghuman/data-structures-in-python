# 1. First, we initialize the number of vertices in the graph.
# 2. Then, we define a dictionary to store the adjacency list.
# 3. Next, we add the edges to the graph.
# 4. Finally, we print the adjacency list.
# Time Complexity: O(V + E)

class Graph:
    def __init__(self, vertices, directed=True):
        self.V = vertices
        self.m_nodes = range(self.V)

        # Define the type of a graph
        # for directed graph   ->  directed = True
        # for undirected graph ->  directed = False
        self.m_directed = directed

        self.m_adj_list = {node: set() for node in self.m_nodes}

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))

    def print_adj_list(self):
        print('\n')
        for key in self.m_adj_list.keys():
            print('node {} : {}'.format(key, self.adj_list[key]))


graph = Graph(5)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_list()
