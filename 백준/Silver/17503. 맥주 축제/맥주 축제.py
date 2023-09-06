import sys
import heapq as hq
input = sys.stdin.readline

N, M, K = map(int, input().split())
beers = []

for _ in range(K):
    v, c = map(int, input().split())
    beers.append((v, c))
    
beers.sort(key=lambda x: (x[1], x[0]))
total_pref = 0
beer_que = []
now_level = 0
isFind = False

for i in range(K):
    preference, alcohol_degree = beers[i]
    total_pref += preference
    now_level = alcohol_degree
    hq.heappush(beer_que, preference)
    
    if len(beer_que) == N:
        if total_pref >= M:
            isFind = True
            break
        else:
            total_pref -= hq.heappop(beer_que) 

if isFind:
    print(now_level)
else:
    print(-1)