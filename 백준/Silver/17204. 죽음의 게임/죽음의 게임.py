import sys
input = sys.stdin.readline

def solution():
    
    
    def dfs(start, num, cnt):
        visit[num] = True
        if num == m:
            return cnt
        
        if num == start:
            return -1
        
        if visit[arr[num]]:
            return -1
        
        return dfs(start, arr[num], cnt+1)
        
    n, m = map(int, input().split())
    visit = [False] * n
    arr = []
    
    for _ in range(n):
        arr.append(int(input()))
    
    return dfs(0, arr[0], 1)
        
print(solution())