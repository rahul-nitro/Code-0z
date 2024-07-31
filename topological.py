from collections import defaultdict

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, frm, to):
        self.graph[frm].append(to)
        if not self.directed:
            self.graph[to].append(frm)

    def topo_sort_visit(self, node, visited, stack):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.topo_sort_visit(neighbor, visited, stack)
        stack.append(node)

    def topo_sort(self):
        visited = {node: False for node in self.graph}

        # Ensure all nodes are included in the visited dictionary
        for neighbors in self.graph.values():
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited[neighbor] = False

        stack = []

        for node in list(self.graph.keys()):
            if not visited[node]:
                self.topo_sort_visit(node, visited, stack)

        return stack[::-1]  # Return in reverse order to get the topological sorting

# Main block
if __name__ == '__main__':
    g = Graph(directed=True)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 4)
    g.add_edge(3, 6)
    g.add_edge(4, 6)
    print("Topological Sort:")
    print(g.topo_sort())