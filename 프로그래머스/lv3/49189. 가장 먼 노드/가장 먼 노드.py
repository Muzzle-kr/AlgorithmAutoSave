import heapq as hq

def solution(n, vertexs):
    
    '''
    1번 노드부터 최단거리로 이동할 수 있는 노드를 찾는다.
    최단거리를 저장하는 배열과 이동 거리를 저장하는 노드를 찾는다.
    다익스트라 알고리즘 + 배열 사용
    '''
    
    
    def dijktra(start):
        d = [INF] * (n+1)
        d[start] = 0    
        heap = []
        
        hq.heappush(heap, (0, start))
        
        while heap:
            dist, cur_node = hq.heappop(heap)
            
            
            for next_node in edges[cur_node]:
                if d[next_node] > dist + 1:
                    d[next_node] = dist + 1
                    hq.heappush(heap, (d[next_node], next_node))
            
        
        max_cnt = max([i for i in d if i != INF])
        return d.count(max_cnt)
        
    answer = 0
    INF = int(1e9)
    edges = [[] for _ in range(n+1)]
    
    for start, end in vertexs:
        edges[start].append(end)
        edges[end].append(start)
        
    
    return dijktra(1)