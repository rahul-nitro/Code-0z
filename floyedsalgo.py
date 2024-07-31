nV = 4
INF = float('inf')

def floydWarshall(graph):
    dist = [[graph[i][j] for j in range(nV)] for i in range(nV)]
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)

# Printing the output
def printSolution(dist):
    for i in range(nV):
        for j in range(nV):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

graph = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

floydWarshall(graph)
