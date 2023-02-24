import heapq as hq

def solution(N, road, K):
    answer = []
    roadInfo = [[] for _ in range(N+1)]
    delivery = [5000001] * (N + 1)
    delivery[1] = 0
    
    def dijkstra():
        heap = []
        hq.heappush(heap, [0, 1])
        
        while heap:
            cost, node = hq.heappop(heap)
            
            for next, distance in roadInfo[node]:
                if  distance + cost <= delivery[next]:
                    delivery[next] = distance + cost
                    hq.heappush(heap, [distance + cost, next])
                            
    for [start, end, distance] in road:
        roadInfo[start].append([end, distance])
        roadInfo[end].append([start, distance])
      
    dijkstra()
    
    return len([i for i in delivery[1:] if i <= K])