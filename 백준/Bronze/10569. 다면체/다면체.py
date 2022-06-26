repeat = int(input())

for i in range(repeat):
    vertex, edge = map(int, input().split())
    side = abs(vertex - edge) + 2
    print(side)
