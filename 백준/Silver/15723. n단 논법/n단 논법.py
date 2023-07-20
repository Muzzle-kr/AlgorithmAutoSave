import sys
import string

input = sys.stdin.readline
INF = int(1e9)
n = int(input())
alphabet = string.ascii_lowercase
graph = [[INF] * (26) for _ in range(26)]

for _ in range(n):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    graph[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    a, b = map(alphabet.index, input().rstrip().split(" is "))
    
    if graph[a][b] == INF:
        print("F")
    else:
        print("T")
