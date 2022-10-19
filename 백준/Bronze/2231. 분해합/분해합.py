dic = {}
for i in range(0, 1000000):
    sum = 0
    sum += i 
    
    for j in str(i):
        sum += int(j)
    if sum not in dic:
        dic[sum] = i
    else:
        if dic[sum] > i:
            dic[sum] = i

num = int(input())

if num in dic:
    print(dic[num])
else:
    print(0)