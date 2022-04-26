N = int(input())
target = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

ans = []
target.sort()

for i in compare:
  start = 0
  end = len(target) - 1
  doesFind = False
  while start <= end:
    mid = (start + end ) // 2
    
    if target[mid] > i:
      end = mid - 1
      continue
    elif target[mid] < i:
      start = mid + 1
      continue
    else:
      ans.append(1)
      doesFind = True
      break
  if not doesFind:
    ans.append(0)
  
print(*ans)