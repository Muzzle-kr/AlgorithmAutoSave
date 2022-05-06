grade = input()

score = 0.0
if grade == 'F':
    print(score)
    exit()
    
alpha = grade[0]
symbol = grade[1]

if alpha == 'A':
    score += 4
elif alpha == 'B':
    score += 3
elif alpha == 'C':
    score += 2
elif alpha == 'D':
    score += 1
    
if symbol == '+':
    score += 0.3
elif symbol == '-':
    score -= 0.3
    
print(score)
