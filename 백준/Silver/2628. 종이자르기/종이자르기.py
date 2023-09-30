w, h = map(int, input().split())
n = int(input())
cut_w = [0, w]
cut_h = [0, h]

for _ in range(n):
    cr, num = map(int, input().split())
    
    if cr == 0:
        cut_h.append(num)
    else:
        cut_w.append(num)
        
cut_w.sort()
cut_h.sort()

max_w = 0
max_h = 0

for i in range(1, len(cut_w)):
    max_w = max(max_w, cut_w[i] - cut_w[i-1])
    
for i in range(1, len(cut_h)):
    max_h = max(max_h, cut_h[i] - cut_h[i-1])

print(max_w * max_h)