import heapq as hq

arr = []
hq.heappush(arr, 64)
x = int(input())

while sum(arr) != x and len(arr) > 0:
    
    # 가장 짧은 막대기를 꺼낸다.
    y = hq.heappop(arr)
    
    # 가장 짧은 막대기를 반으로 자른다.
    y = y//2
    
    # 남은 막대와 + 짧은 막대기가 X보다 크거나 같다면 반쪽만 다시 넣기
    if sum(arr) + y >= x:
        hq.heappush(arr, y)
    # x가 더 크다면 자른 걸 둘 다 넣기
    else:
        hq.heappush(arr, y)
        hq.heappush(arr, y)
        
print(len(arr))