
highestScore = (0, 0)

for i in range(5):
  score = sum(list(map(int, input().split())))

  if score > highestScore[1]:
    highestScore = (i + 1, score)
    

print(*highestScore)