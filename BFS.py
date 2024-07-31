graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)

    return visited

# Main module
if __name__ == '__main__':
    print("Following is the Breadth-First Search:")
    bfs_result = bfs(graph, '5')
    print(" ".join(bfs_result))
