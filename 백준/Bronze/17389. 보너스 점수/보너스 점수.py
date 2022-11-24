N = int(input())
S = input()

bonus = 0
total = 0
for idx, s in enumerate(S):
    score = idx + 1
    
    if s == "O":
        total += score
        total += bonus
        bonus += 1
    else:
        bonus = 0
        
print(total)
    