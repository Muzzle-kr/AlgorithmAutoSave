import math

N = int(input())
M = list(map(int, input().split()))
budget = int(input())

M.sort()
low = 0
high = max(M)
ans = 0

while low <= high:
  mid = (low + high) // 2
  totalBudget = 0
  for region in M: 
    totalBudget += min(region, mid)
  
  if totalBudget > budget:
    high = mid-1
  else:
    low = mid + 1
    ans = mid

print(ans)
