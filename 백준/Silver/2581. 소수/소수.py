import heapq as hq
import math
import sys

input = sys.stdin.readline
bottom = int(input())
top = int(input())
primeArr = []


def findPrimeNumber(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    isPrimeNumber = False
    for i in range(3, math.ceil(math.sqrt(num))+1):
        if num % i == 0:
            return False
        else: 
            continue
        
    if isPrimeNumber == False:
        return True

for i in range(bottom, top + 1):
    if findPrimeNumber(i):
        hq.heappush(primeArr, i)
        
if len(primeArr) == 0:
    print(-1)
else:
    print(sum(primeArr))
    print(primeArr[0])
    