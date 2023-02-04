import sys
input = sys.stdin.readline

N = int(input())

stoneBridge = list(map(int, input().split()))
visit = [0 for _ in range(N + 1)]
sp = int(input()) - 1
visit[sp] = 1

result = 0


def dfs(p):
    
    cnt = 1
    jump = stoneBridge[p]
    
    # print(f'p {p}, count: {count}, jump: {jump}')
    
    if 0 <= p + jump < N and visit[p + jump] == 0:
      visit[p + jump] = 1
      # print(f'{p} 지점에서  {jump}칸 앞으로 점프합니다.')
      cnt += dfs(p + jump)
    if 0 <= p - jump < N and visit[p - jump] == 0:
      visit[p - jump] = 1
      # print(f'{p} 지점에서  {jump}칸 뒤로 점프합니다.')
      cnt += dfs(p - jump)
    
    return cnt
    # countArr.append(count)
    
result += dfs(sp)

print(result)