fibArr = [0, 1, 1]

num = int(input())


if num >= 3:
    for i in range(3, num+1):
        fibArr.append(fibArr[i-2] + fibArr[i-1])

print(fibArr[num])