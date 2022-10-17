count = 0
num = int(input())

while True:
    if num == 1:
        break
    
    if num % 2 == 0:
        num = num // 2
        count += 1
    else:
        num += 1
        count += 1

print(count)