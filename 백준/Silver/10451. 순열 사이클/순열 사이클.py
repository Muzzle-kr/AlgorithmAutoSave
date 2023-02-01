def dfs(num):
    
    chk[num] = 1
    
    for i in dimensionList[num]:
        if chk[i] == 0:
            dfs(i)
    
for i in range(int(input())):
    answer = 0
    num = int(input())
    arr = [i+1 for i in range(num)]
    randomPermutation = list(map(int, input().split()))
    chk = [0] * (num + 1)    
    dimensionList = [[] for i in range(num + 1)]
    
    for i in range(num):
        a = arr[i]
        r = randomPermutation[i]

        dimensionList[a].append(r)
        dimensionList[r].append(a)
    
    for i in range(1, num + 1):
        for j in dimensionList[i]:
            if chk[j] == 0:
                answer += 1
                dfs(j)
                
    print(answer)