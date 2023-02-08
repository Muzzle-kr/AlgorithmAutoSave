import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

students = []
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
positions = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))


def checkDasomPa(comb):
    
    dasom = 0
    for (x, y) in comb:
        if students[x][y] == 'S':
            dasom += 1
        
        if dasom >= 4:
            return True
    return False
    

def checkAdjacent(comb):
    visit = [False] * 7
    q = deque()
    q.append(comb[0])
    visit[0] = True
    
    
    while q:
        x, y = q.popleft()

        for (dx, dy) in direction:
            nx = x + dx
            ny = y + dy
            
            if (nx, ny) in comb:                
                nextIdx = comb.index((nx, ny))
                if not visit[nextIdx]:
                    visit[nextIdx] = True
                    q.append((nx, ny))  
    return False if False in visit else True


for _ in range(5):
    students.append(list(input().strip()))
    

count = 0

for comb in combs:
    if checkDasomPa(comb):
        if checkAdjacent(comb):
            count += 1

print(count)     
    