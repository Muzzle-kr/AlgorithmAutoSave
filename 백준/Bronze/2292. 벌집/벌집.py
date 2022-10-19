num = int(input())
arr = [1]
sum = 1
for i in range(1, 1000000):
    sum += i * 6
    arr.append(sum)
    
for idx, i in enumerate(arr):
    if num <= i:
        print(idx + 1)
        break