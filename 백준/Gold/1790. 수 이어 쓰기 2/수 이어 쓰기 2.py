import math
m, n = map(int, input().split())
# n = int(input())

'''
1 ~ 9 ->        count 9       digit 1 -> total 9  
10 ~ 99 ->      count 90      digit 2 -> total 180
100 -> 999 ->   count 900     digit 3 -> total 2700 
'''
count, digit, total, start = 0, 0, 0, 0

while True:
    digit += 1
    count = 9 * (10 ** (digit - 1))
    total += (count * digit)
    if total >= n:
        total -= (count * digit)
        break
    start += count

nth = (n - total - 1) // digit
order = (n - total - 1) % digit
targetNumber = start + nth + 1
# print(f'count: {count}, digit: {digit}, total: {total}, nth: {nth}, order: {order}, start: {start}, targetNumber: {targetNumber}')

if targetNumber > m:
    print(-1)
else:
    print(str(targetNumber)[order])