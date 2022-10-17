from math import sqrt

x1,y1,r1 = map(int, input().split())
x2,y2,r2 = map(int, input().split())

distance = sqrt((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2))
rSum = r1 + r2

if distance < rSum:
    print("YES")
else:
    print("NO")