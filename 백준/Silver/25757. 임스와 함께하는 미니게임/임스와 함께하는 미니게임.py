N, G = input().split()

numOfPeople = {
    "Y": 2,
    "F": 3,
    "O": 4,
}

already_played = {}
cnt = 1
ans = 0

for _ in range(int(N)):
    player = input()
    
    if player in already_played:
        continue
    
    cnt += 1
    already_played[player] = 1
    
    if cnt == numOfPeople[G]:
        cnt = 1
        ans += 1
        continue
    
print(ans)