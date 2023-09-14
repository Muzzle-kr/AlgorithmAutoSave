n = int(input())

pillars = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])

max_height = 0
max_height_idx = 0

for i in range(n):
    if pillars[i][1] > max_height:
        max_height = pillars[i][1]
        max_height_idx = i
        
ans = 0
prev_w, prev_h = pillars[0][0], pillars[0][1]

for i in range(1, max_height_idx + 1):
    w, h = pillars[i][0], pillars[i][1]
    
    if h >= prev_h:
        ans += (w - prev_w) * prev_h
        prev_w, prev_h = w, h

prev_w, prev_h = pillars[-1][0], pillars[-1][1]

for i in range(n-2, max_height_idx-1, -1):
    w, h = pillars[i][0], pillars[i][1]
    
    if h >= prev_h:
        ans += (prev_w - w) * prev_h
        prev_w, prev_h = w, h

print(ans + max_height)
    
    