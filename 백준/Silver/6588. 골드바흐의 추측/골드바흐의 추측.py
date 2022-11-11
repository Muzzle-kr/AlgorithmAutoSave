import sys
input = sys.stdin.readline

# 에라토스테네스의 체
primeArr = [0 for i in range(1000001)]
num = 1000000

for i in range(num + 1):
    primeArr[i] = i
            
for i in range(3, num + 1):
    if primeArr[i] == 0: continue
    for j in range(i + i, num + 1, i):
        primeArr[j] = 0

primeArr[1] = 0
primeArr[2] = 0

while True:
    maxDiff = 0
    n = int(input())
    result = [0, 0]
    
    if n == 0:
        break
    
    # b가 젤 크고 a가 젤 작으면 바로 out
    isFind = False
    for i in range(3, len(primeArr)):
        if primeArr[i] != 0 and primeArr[n-i] != 0:   
            print(f'{n} = {primeArr[i]} + {primeArr[n-i]}')
            isFind = True
            break
    if not isFind:
        print("Goldbach's conjecture is wrong.")

