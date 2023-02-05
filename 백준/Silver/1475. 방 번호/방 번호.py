import math
dict = {}

for i in range(10):
    dict[str(i)] = 0

for i in list(input()):    
    dict[i] += 1

# 6이랑 9 합치기
dict["6"] = math.ceil((dict["6"] + dict["9"]) / 2)
dict.pop("9")
result = sorted(dict.values(), reverse=True)

print(result[0])


