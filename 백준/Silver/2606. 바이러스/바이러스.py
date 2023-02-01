numberOfComputer = int(input())
numberOfNetworks = int(input())
network = [[] for _ in range(numberOfComputer + 1)]
chk = [0] * (numberOfComputer + 1)
answer = 0

def dfs(n):
    global answer
    answer += 1
    chk[n] = 1
    
    for i in network[n]:
        if chk[i] == 0:
            dfs(i)
    
    
for i in range(numberOfNetworks):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

chk[1] = 1

for i in network[1]:
    if chk[i] == 0:
        dfs(i)

print(answer)