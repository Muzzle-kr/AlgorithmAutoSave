arr = [1, 3]
num = 9780921418
sum = 0

for idx, i in enumerate(str(num)):
    rest = idx % 2
    sum += (arr[rest] * int(i))
    
sum += int(input()) * 1
sum += int(input()) * 3
sum += int(input()) * 1
print(f'The 1-3-sum is {sum}')