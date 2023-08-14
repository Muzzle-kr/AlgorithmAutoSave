import sys
input = sys.stdin.readline
N = int(input())
flowers = []

for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((sm*100+sd, em*100+ed))
    
flowers.sort(key=lambda x: (x[0], x[1]))
last_end = 301
end = 0
cnt = 0

while flowers:
    if last_end >= 1201 or last_end < flowers[0][0]:
        break
    
    for i in range(len(flowers)):
        if last_end >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]

            flowers.remove(flowers[0])
        else:
            break
        
    
    last_end = end
    cnt += 1

if last_end < 1201:
    print(0)
else:    
    print(cnt)