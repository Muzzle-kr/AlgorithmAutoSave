# 에라토스테네스의 체
import math
arr = [0 for i in range(123456 * 2 + 1)]
num = 123456 * 2

for i in range(num):
    arr[i] = i

for i in range(2, num + 1):
    if arr[i] == 0:
        continue
    for j in range(i + i, num + 1, i):
        arr[j] = 0

# for i in range(2, num + 1):
#     if arr[i] != 0:
#         # print(f'{arr[i]}')


while True:
    n = int(input())
    
    if n == 0:
        break
    
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if arr[i] != 0:
            count += 1
    
    print(count)