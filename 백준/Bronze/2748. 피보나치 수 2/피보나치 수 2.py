num = int(input())

memo = [0, 1, 1]
for i in range(3, num + 1):
  try:
    if memo[i]:
      continue;
  except:
    memo.append((memo[i-2] + memo[i-1])) 

print(memo[num])