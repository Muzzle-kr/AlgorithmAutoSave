import heapq

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1]))
p_arr=[]

for i in arr:
    heapq.heappush(p_arr, i[0])
    
    if (len(p_arr) > i[1]):
        heapq.heappop(p_arr)

print(sum(p_arr))