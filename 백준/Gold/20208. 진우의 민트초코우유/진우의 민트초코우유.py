n, initial_hp, stamina = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def cal_dist(x, y, dx, dy):
    return abs(x - dx) + abs(y - dy)

def dfs(x, y, hp, milk):
    global answer
    
    for mx, my in mint_milk:
        if graph[mx][my] == 2:
            dist = cal_dist(x, y, mx, my)
            if dist <= hp:
                # 민트 우유 마시기
                graph[mx][my] = 0
                dfs(mx, my, hp - dist + stamina, milk + 1)
                graph[mx][my] = 2
    
    # 많이 먹은 우유 갯수 갱신
    if cal_dist(x, y, hx, hy) <= hp:
        answer = max(answer, milk)
hx, hy = 0, 0
mint_milk = []

for i in range(n):
    for j in range(n):
        
        # 진우의 집 찾기
        if graph[i][j] == 1:    
            hx, hy = i, j
        # 우유가 있는 위치 찾기
        elif graph[i][j] == 2:
            mint_milk.append((i, j))

dfs(hx, hy, initial_hp, 0)
print(answer)