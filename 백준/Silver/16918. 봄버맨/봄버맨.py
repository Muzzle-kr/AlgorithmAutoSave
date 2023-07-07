bomb = {}
empty = []

r, c, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for i in range(r):
    for j in range(c):
        if graph[i][j] == "O":
            bomb[(i, j)] = 3
        else:
            empty.append((i, j))

def boom(x, y):
    graph[x][y] = '.'
    empty.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < r and 0 <= ny < c:
            graph[nx][ny] = '.'
            empty.append((nx, ny))
    return

def install_bomb():
    global empty
    # 빈칸에 폭탄 설치하기
    for x, y in empty:
        graph[x][y] = "O"
        bomb[(x, y)] = 3
    empty = []

second = 0

def print_graph(second):
    # print(f'--------{second}초 후 graph')
    for g in graph:
        for k in g:
            print(k, end="")
        print()
        
def minus_bomb_time():
    for (x, y), time in bomb.items():
        bomb[(x, y)] -= 1

def explode_bomb():
    del_list = []
    
    for (x, y), time in bomb.items():
        if bomb[(x, y)] == 0:
            boom(x, y)
            del_list.append((x, y))
    
    for x, y in del_list:
        del bomb[(x, y)]
            
if n == 1: # 1초 뒤라면 그대로 출력
    print_graph(second)
        
elif n == 2: # 2초 뒤라면 모든 칸에 폭탄이 설치되어 있음
    for i in range(r):
        print("O"*c)

else: # 3초 이상일 경우
    second = 1
    minus_bomb_time()
    # print_graph(second)
    
    while second < n:
        minus_bomb_time()
        second += 1
        
        if second % 2 == 0: # 짝수 초라면 빈 칸에 폭탄 설치하기
            install_bomb()
        else: # 홀수초라면 폭탄 터뜨리기
            explode_bomb()

    print_graph(second)