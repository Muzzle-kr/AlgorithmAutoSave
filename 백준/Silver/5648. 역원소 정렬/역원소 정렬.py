import heapq as hq

result = []

arr = list
break_point = 0
count = 0
while True:
        arr = list(map(int, input().split()))
        
        if count == 0:
            break_point = arr[0]
            arr = arr[1:]
        
        for i in arr:
            count += 1
            tmp = ""
            
            for j in str(i):
                tmp = j + tmp
            
            hq.heappush(result, int(tmp))
        
        if count == break_point:
            break

for i in range(len(result)):
    print(hq.heappop(result))