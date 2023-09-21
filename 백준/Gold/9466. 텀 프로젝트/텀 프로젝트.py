import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
    global count
    cycle_list.append(n)
    visited[n] = True
    
    x = arr[n]
    
    if visited[x]:
        if x in cycle_list:
            count -= len(cycle_list[cycle_list.index(x):])
            return
    else:
        dfs(x)
    
for _ in range(int(input())):
    N = int(input().rstrip())
    arr = [0] + list(map(int, input().rstrip().split()))
    
    visited = [False] * (N+1)
    count = N
    
    for i in range(1, N+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)
    
    print(count)