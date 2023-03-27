import heapq as hq
import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    vertex = []
    edges = [[] for _ in range(N+1)]
    visit = [False] * (N+1)
    answer = []
    mst = []
    
    
    for _ in range(M):
        s, e, d = map(int, input().split())
        edges[s].append((d, e))
        edges[e].append((d, s))


    # 정점 1 방문처리
    for d, e in edges[1]:
        hq.heappush(vertex, (d, e))
    visit[1] = True
    
    while vertex:
        cost, node = hq.heappop(vertex)

        if not visit[node]:    
            answer.append(cost)
            visit[node] = True
            
            if len(answer) == N:
                break
            
            for d, e in edges[node]:
                # 방문하지 않은 노드만 추가
                if not visit[e]:
                    hq.heappush(vertex, (d, e))
    return sum(answer) - max(answer)

print(solution())