import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))
    maxCosts = 0
    earn = 0
    
    for i in range(n-1, -1, -1):
        if stocks[i] == maxCosts:
            continue
        elif stocks[i] > maxCosts:
            maxCosts = stocks[i]
        else:
            earn += maxCosts - stocks[i]
    print(earn)