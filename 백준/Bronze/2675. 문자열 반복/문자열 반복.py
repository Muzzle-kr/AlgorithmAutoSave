N = int(input())

result = []
for _ in range(N):
  li = input().split()
  repeat = int(li[0])
  word = li[1::]
  sentence = ""
  for i in range(len(word[0])):
    syl = word[0][i]
    for _ in range(repeat):
      sentence += syl
  result.append(sentence)

print(*result)