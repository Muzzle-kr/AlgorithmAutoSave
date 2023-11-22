n, w, l = map(int, input().split())
queue = []
weights = []
arr = list(map(int, input().split()))
time = 0

while arr:
    # queue 앞으로 한칸씩 이동
    idx_correction = 0
    for i in range(len(queue)):
        i -= idx_correction
        queue[i] += 1 
        
        if queue[i] == w:
            weights.pop(0)
            queue.pop(0)
            idx_correction += 1
        
    if sum(weights) + arr[0] <= l:
        weights.append(arr[0])
        queue.append(0)
        arr.pop(0)
    
    time += 1

time += (w - queue[-1])
print(time)