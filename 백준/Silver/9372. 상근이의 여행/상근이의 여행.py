
def dfs(x):
    cnt = 1
    cities[x] = 1
    
    # print(f'x: {x}')
    for air in airplane[x]:
        if not cities[air]:
            cnt += dfs(air)
    # print(f'x: {x}, cnt: {cnt}')
    return cnt
for _ in range(int(input())):
    n, m = map(int, input().split())
    airplane = [[] for _ in range(n+1)]
    cities = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        airplane[a].append(b)
        airplane[b].append(a)
    
    result = -1
    
    for air in airplane:
        for a in air:
            if not cities[a]:
                result += dfs(a)
    print(result)