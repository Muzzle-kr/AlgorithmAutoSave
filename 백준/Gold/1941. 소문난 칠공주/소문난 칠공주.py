from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline
students = []
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
orders = [(i, j) for i in range(5) for j in range(5)]
lists = combinations(orders, 7)
answer = 0

for i in range(5):
    students.append(list(input().strip()))


def checkOverFourDasom(arr):    
    count = 0
    
    for (x, y) in arr:    
        if students[x][y] == "S":
            count += 1        
        if count >= 4: return True
    return False

def checkAdjacent(arr):
    visit = [False] * 7
    q = deque()
    q.append(arr[0])
    visit[0] = True
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            
            foundIndex = -1
            for idx, i in enumerate(arr):
                if i == (nx, ny):
                    foundIndex = idx

            if foundIndex != -1 and visit[foundIndex] == False:
                visit[foundIndex] = True
                q.append((nx, ny))
    
    return True if False not in visit else False

for c in lists:
    if checkOverFourDasom(c):
        if checkAdjacent(c):
            answer += 1

print(answer)