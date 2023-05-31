mbti = [["E", "I"], ["S", "N"], ["F", "T"], ["J", "P"]]
yg = input()
ans = ""
for idx, a in enumerate(yg):
    ans += mbti[idx][not mbti[idx].index(a)]
    
print(ans)