import heapq as hq
N = int(input())

arr = []
for _ in range(N):
    hq.heappush(arr, int(input()))

idx = 0
total = 0
while len(arr) > 1:
    n1 = hq.heappop(arr)
    n2 = hq.heappop(arr)
    
    total += n1 + n2
    # print(f'total:', total)
    hq.heappush(arr, n1 + n2)
    idx += 1

print(total)



# 10 20
# 30 30
# 60 40
# 100 50

# 190
# 150