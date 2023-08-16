n = int(input())
plus = []
minus = []
zero = 0

for _ in range(n):
    num = int(input())
    if num >= 1:
        plus.append(num)
    elif num < 0:
        minus.append(-num)
    else:
        zero += 1

total = 0
plus.sort(reverse=True)
minus.sort(reverse=True)

for i in range(0, len(plus), 2):
    if i + 1 < len(plus):
        if plus[i] == 1 or plus[i+1] == 1:
            total += plus[i] + plus[i+1]
        else:
            total += plus[i] * plus[i + 1]
    else:
        total += plus[i]

for i in range(0, len(minus), 2):
    if i + 1 < len(minus):
        total += minus[i] * minus[i + 1]
    else:
        if zero > 0:
            zero -= 1
        else:
            total -= minus[i]
print(total)