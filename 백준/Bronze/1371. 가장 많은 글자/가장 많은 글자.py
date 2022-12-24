import sys
sentence = sys.stdin.read()
sentence = sentence.replace("\n", "").replace(" ", "")
dictionary = {}

for w in sentence:
    if w in dictionary:
        dictionary[w] += 1
    else:
        dictionary[w] = 1 

# dictionary 최대값 추출
largest = max(dictionary.values())

# 최대값 순으로 정렬
dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

# 결과를 담을 배열 
result = []

# dict을 돌면서 최대값은 result.append, 최소값을 찾으면 바로 종료
for w in dictionary:
    if w[1] == largest:
        result.append(w[0])
    else:
        break

# 사전순 정렬
result.sort()

for i in result:
    print(i, end="")