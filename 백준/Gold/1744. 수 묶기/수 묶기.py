N = int(input())

plus = []
minus = []
zero = 0
for _ in range(N):
    n = int(input())
    
    if n > 0:
        plus.append(n)
    elif n < 0:
        minus.append(n)
    else:
        zero += 1
        
plus.sort(reverse=True)
minus.sort()

total = 0

for i in range(0, len(plus), 2):
    if i+1 < len(plus):
        total += max(plus[i] * plus[i+1], plus[i] + plus[i+1])
    else:
        total += plus[i]
    

for i in range(0, len(minus), 2):
    if i+1 < len(minus):
        total += minus[i] * minus[i+1]
    else:
        if zero > 0:
            zero -= 1
        else:
            total += minus[i]

print(total)