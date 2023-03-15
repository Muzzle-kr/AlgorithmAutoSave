import heapq as hq

def solution(n, works):
    arr = []
    
    if sum(works) < n:
        return 0
    
    for w in works:
        hq.heappush(arr, -w)
        
    while n:
        num = hq.heappop(arr)
        num += 1
        
        hq.heappush(arr, num)
        n -= 1
    
    return sum([i ** 2 for i in arr])