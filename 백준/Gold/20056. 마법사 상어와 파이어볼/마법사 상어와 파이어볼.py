N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    # 행, 열, 질량, 속력, 방향
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r, c, m, s, d])

# 북, 북동, 동, 남동, 남, 남서, 서, 북서
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


for p in range(K):
    graph = [[[] for _ in range(N)] for _ in range(N)]
    add = []
    
    for i in range(len(fireballs)):
        r, c, m, s, d = fireballs[i]
        
        nx = (r + dx[d] * s) % N
        ny = (c + dy[d] * s) % N
        
        graph[nx][ny].append((m, s, d))
        # 추가, 삭제 대상 추가        
    
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) > 1:
                # 질량, 속력, 방향
                m_sum = 0
                s_sum = 0
                d_list = []
                
                for k in range(len(graph[i][j])):
                    m, s, d = graph[i][j][k]
                    m_sum += m
                    s_sum += s
                    d_list.append(d)
                
                m = m_sum // 5
                s = s_sum // len(graph[i][j])
                
                if m == 0:
                    continue
                
                # 방향
                pair_cnt = 0
                odd_cnt = 0
                for d in d_list:
                    if d % 2 == 0:
                        pair_cnt += 1
                    else:
                        odd_cnt += 1
                
                if pair_cnt == len(d_list) or odd_cnt == len(d_list):
                    add.append([i, j, m, s, 0])
                    add.append([i, j, m, s, 2])
                    add.append([i, j, m, s, 4])
                    add.append([i, j, m, s, 6])
                else:
                    add.append([i, j, m, s, 1])
                    add.append([i, j, m, s, 3])
                    add.append([i, j, m, s, 5])
                    add.append([i, j, m, s, 7])
            else:
                if len(graph[i][j]) == 1:
                    m, s, d = graph[i][j][0]
                    add.append([i, j, m, s, d])
    
    if p == K - 1:
        result = 0
        for i in range(len(add)):
            result += add[i][2]
        print(result)
    fireballs = add
