N = int(input())
import math
for _ in range(N):
    sum = 0
    digit = input()
    
    for idx, i in enumerate(digit):
        idx = 23 - idx
        if int(i) == 1:
            sum += math.pow(2, idx)
            
    print(int(sum))