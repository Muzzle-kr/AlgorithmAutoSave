import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

num = int(input())
me, target = map(int, input().split())
relation = int(input())
dimensionList = [[] for i in range(num + 1)]
chk = [0 for i in range((num + 1))]
answer = -1

def dfs(num):
    global chon
    global answer
    chon += 1
    chk[num] = 1
    
    for i in dimensionList[num]:
        if chk[i] == 0:
            if i == target:
                answer = chon
            dfs(i)
            chon -= 1
for i in range(relation):
    a, b = map(int, input().split())
    
    dimensionList[a].append(b)
    dimensionList[b].append(a)

# print(f'dimensionList: {dimensionList}')
for i in dimensionList[me]:
    chon = 1
    if chk[i] == 0:
        if i == target:
            answer = chon
            break
        
        dfs(i)

print(answer)