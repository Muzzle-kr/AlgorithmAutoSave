S = input()
ans = 0

for i in range(1, 30000):
    if S == "":
        ans = i - 1
        break
    
    idx = 0
    cnt = 0
    
    for j in range(len(str(i))):
        if idx >= len(S):
            break
        if S[idx] == str(i)[j]:
            cnt += 1
            idx += 1
    
    S = S[idx:]

print(ans)
    
    