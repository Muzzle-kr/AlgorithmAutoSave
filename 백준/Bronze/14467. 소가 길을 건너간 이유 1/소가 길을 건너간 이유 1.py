ans = 0
dic = {}

for _ in range(int(input())):
    n, d = map(int, input().split())
    
    if n in dic:
        if dic[n] != d:
            ans += 1
        dic[n] = d
    else:
        dic[n] = d
print(ans)