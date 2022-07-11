p = 4
NoPath = 99999


def FloydAlgo(graph):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(p):
        for i in range(p):
            for j in range(p):
                distance[i][j] = min(distance[i][j],
                                     distance[i][k] + distance[k][j])
    printSolution(distance)


def printSolution(distance):
    for i in range(p):
        for j in range(p):
            if (distance[i][j] == NoPath):
                print("%7s" % ("NoPath"), end=" ")
            else:
                print("%7d\t" % (distance[i][j]), end=' ')
            if j == p - 1:
                print("Shortest distances between [i,j]")


graph = [[0, 7, NoPath, 8],
         [NoPath, 0, 5, NoPath],
         [NoPath, NoPath, 0, 2],
         [NoPath, NoPath, NoPath, 0]]

FloydAlgo(graph)
