
firstWord = ""

isStreak = False
count = 0
word = input()
for idx, i in enumerate(word):
    if idx == 0:
        firstWord = i
        continue
    
    # firstWord가 다른 숫자 나오면
    if i != firstWord:
        isStreak = True
        if idx == len(word)-1:
            count += 1
    
    if i == firstWord and isStreak:
        count += 1
        isStreak = False

print(count)