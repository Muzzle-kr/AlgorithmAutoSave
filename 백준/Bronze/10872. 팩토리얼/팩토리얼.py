num = int(input())

memo = [1, 1, 2]

for i in range(3, num + 1):
    try:
        if memo[i]:
            continue
    except: 
        memo.append(i * memo[i-1])

print(memo[num])