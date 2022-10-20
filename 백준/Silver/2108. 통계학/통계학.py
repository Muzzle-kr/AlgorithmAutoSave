arr = []
dicts = {}

for _ in range(int(input())):
    num = int(input())
    arr.append(num)
    
    if num not in dicts:
        dicts[num] = 1
    else:
        dicts[num] += 1

arr.sort()

sortedDict = sorted(dicts.items(), key=lambda x: (-x[1], x[0]))
# print(sortedDict)
print(int(round(sum(arr)/len(arr), 0)))
print(arr[len(arr)//2])
if len(sortedDict) > 1:
    if sortedDict[0][1] == sortedDict[1][1]:
        print(sortedDict[1][0])
    else:
        print(sortedDict[0][0])
else:
    print(sortedDict[0][0])
print(max(arr) - min(arr))