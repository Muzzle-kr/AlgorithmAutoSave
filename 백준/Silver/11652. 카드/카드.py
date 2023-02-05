
dict = {}

for _ in range(int(input())):
    num = int(input())
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
        

arr = sorted(dict.items(), key=lambda x: (-x[1], x[0]))

print(arr[0][0])