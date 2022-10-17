import math

num = int(input())
sum = 0

for i in str(num):
    sum += int(math.pow(int(i), 5))

print(sum)