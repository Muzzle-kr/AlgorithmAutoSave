K = int(input())
n = int(input()) # 가로 줄 수
end = list(input().strip())
start = sorted(end)
ladder = [list(input().strip()) for _ in range(n)]
ladderS = []
ladderE = []

for i in range(n):
    if ladder[i][0] == "?":
        ladderS = ladder[:i]
        ladderE = ladder[i+1:]
        break

# 끝 사다리는 거꾸로 돌린다
ladderE.reverse()


for lad in ladderS:
    for i in range(K-1):
        if lad[i] == "-":
            start[i], start[i+1] = start[i+1], start[i]

for lad in ladderE:
    for i in range(K-1):
        if lad[i] == "-":
            end[i], end[i+1] = end[i+1], end[i]

answer = []

for i in range(K-1):
    if start[i] == end[i]:
        answer.append("*")
    else:
        if start[i] == end[i+1]:
            answer.append("-")
        elif start[i] == end[i-1]:
            answer.append("*")
        else:
            answer = ["x" for _ in range(K-1)]
            break
        
print("".join(answer))
    
    