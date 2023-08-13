import heapq as hq

N = int(input())
q = []

for _ in range(N):
    start, end = map(int, input().split())
    q.append((start, end))
    
q.sort(key=lambda x: (x[0]))

class_room = []
hq.heappush(class_room, q[0][1])

for i in range(1, N):
    start, end = q[i]
    
    if start < class_room[0]:
        hq.heappush(class_room, end)
    else:
        hq.heappop(class_room)
        hq.heappush(class_room, end)

print(len(class_room))