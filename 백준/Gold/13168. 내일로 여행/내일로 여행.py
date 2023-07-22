from collections import defaultdict

# 모든 목적지에서 각각의 목적지로 가는 최소 비용을 먼저 구하기

free_train = ['ITX-Saemaeul', 'ITX-Cheongchun', 'Mugunghwa']
sale_train = ['S-Train', 'V-Train']

# 입력 받기
n, r = map(int, input().split())
cities = list(input().split())
m = int(input())
travel_cities = list(input().split())
k = int(input())

# defaultdict 생성
trains = defaultdict(list)
INF = int(1e9)
dist = [[[INF, INF] for _ in range(n)] for _ in range(n)]

# 열차 정보 입력 받기
for _ in range(k):
    t, s, e, c = input().split()
    
    is_free = True if t in free_train else False
    is_sale = True if t in sale_train else False
    
    s_idx = cities.index(s) # 출발지 인덱스
    e_idx = cities.index(e) # 도착지 인덱스
    
    cost = int(c)
    
    # 일반 금액 처리
    dist[s_idx][e_idx][0] = min(dist[s_idx][e_idx][0], cost)
    dist[e_idx][s_idx][0] = min(dist[e_idx][s_idx][0], cost)
    
    if is_free:
        cost = 0
    elif is_sale:
        cost = cost/2
    
    # 할인 금액 처리
    dist[s_idx][e_idx][1] = min(dist[s_idx][e_idx][1], cost)
    dist[e_idx][s_idx][1] = min(dist[e_idx][s_idx][1], cost)

# 큰 값으로 초기화
INF = int(1e9)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j][0] = min(dist[i][j][0], dist[i][k][0] + dist[k][j][0])
            dist[i][j][1] = min(dist[i][j][1], dist[i][k][1] + dist[k][j][1])


normal_result = 0
sale_result = 0

for i in range(m-1):
    start, end = travel_cities[i], travel_cities[i+1]
    
    s_idx = cities.index(start)
    e_idx = cities.index(end)
    
    normal_result += dist[s_idx][e_idx][0]
    sale_result += dist[s_idx][e_idx][1]

if normal_result > sale_result + r:
    print("Yes")
else:
    print("No")