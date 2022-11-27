# 0이 포함되어있지 않으면 -1

s = input()

if "0" not in s:
    print(-1)
    exit()

s = sorted(list(s), reverse=True)

sum = 0

for i in s:
    i = int(i)
    sum += i
    
if sum % 3 != 0:
    print(-1)
else:
    print("".join(s))