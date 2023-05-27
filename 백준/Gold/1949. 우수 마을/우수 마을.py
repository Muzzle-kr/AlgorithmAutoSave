import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = 1
    for u in g[cur]:
        if not visited[u]:
            dfs(u)
            dp[cur][1] += dp[u][0] # 현재 마을을 우수마을로 선정
            dp[cur][0] += max(dp[u][0], dp[u][1]) # 현재 마을을 우수마을로 선정 X


n = int(input().strip())
people = [0] + [int(x) for x in input().split()]
visited = [0 for _ in range(n+1)]

# dp[i][0] = i마을을 선정X, dp[i][1] = i마을을 선정O
dp = [[0, people[i]] for i in range(n+1)] 
g = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

dfs(1)
print(max(dp[1][1], dp[1][0]))