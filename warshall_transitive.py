class Graph:
    def __init__(self, vertices):
        self.V = vertices

    def print_solution(self, reach):
        print("Following matrix is the transitive closure of the given graph:")
        for i in range(self.V):
            for j in range(self.V):
                print("%7d" % (reach[i][j]), end=" ")
            print()

    def transitive_closure(self, graph):
        reach = [row[:] for row in graph]
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        self.print_solution(reach)

# Main module
if __name__ == '__main__':
    g = Graph(4)
    graph = [
        [1, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1]
    ]
    g.transitive_closure(graph)
