N = int(input())
rightAnswer = list(input())

adrian = ["A", "B", "C"]
bruno = ["B", "A", "B", "C"]
goran = ["C", "C", "A", "A", "B", "B"]

adrianScore = 0
brunoScore = 0
goranScore = 0

for idx, answer in enumerate(rightAnswer):
    if answer == adrian[idx % len(adrian)]:
          adrianScore += 1
    
    if answer == bruno[idx % len(bruno)]:
          brunoScore += 1
    
    if answer == goran[idx % len(goran)]:
          goranScore += 1

largeScore = max(adrianScore, brunoScore, goranScore)

print(largeScore)
if largeScore == adrianScore:
      print("Adrian")

if largeScore == brunoScore:
      print("Bruno")

if largeScore == goranScore:
      print("Goran")
