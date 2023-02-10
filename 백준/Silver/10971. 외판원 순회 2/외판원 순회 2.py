import sys

input = sys.stdin.readline
N = int(input())
cities = []
min_cost = sys.maxsize

for i in range(N):
    cities.append(list(map(int, input().split())))
    

def func(start, next, cost, visit):
    global min_cost
    
    if len(visit) == N:
        if cities[next][start] != 0:
            min_cost = min(min_cost, cost + cities[next][start])
    
    for n in range(N):
        if cities[next][n] != 0 and n not in visit and cost < min_cost:
            visit.append(n)
            func(start, n, cost + cities[next][n], visit)
            visit.pop()
            
for i in range(N):
    func(i, i, 0, [i])
    
print(min_cost)