n = int(input())
memo = [1, 1, 2, 5]
answer = 0

for i in range(4, n+1):
    tot = 0
    
    for j in range(i):
        tot += memo[j] * memo[i-j-1]
    
    memo.append(tot)

print(memo[n])