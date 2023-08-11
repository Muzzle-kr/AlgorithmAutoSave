import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
arr = [0] * 10
    
for i in range(R):
    for j in range(C-2, 0, -1):
        if graph[i][j] != '.' :
            arr[int(graph[i][j])] = C - j
            break

sorted_set_arr = sorted(list(set(arr[1:])))

for i in range(1, 10):
    print(sorted_set_arr.index(arr[i]) + 1)