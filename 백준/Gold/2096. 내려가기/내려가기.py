import sys
input = sys.stdin.readline

n = int(input())

max_result = [0] * 3
min_result = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for _ in range(n):
    a, b, c = map(int, input().split())
    
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_result[j], max_result[j+1])
            min_tmp[j] = a + min(min_result[j], min_result[j+1])
        elif j == 1:
            max_tmp[j] = b + max(max_result[j-1], max_result[j], max_result[j+1])
            min_tmp[j] = b + min(min_result[j-1], min_result[j], min_result[j+1])
        else:
            max_tmp[j] = c + max(max_result[j-1], max_result[j])
            min_tmp[j] = c + min(min_result[j-1], min_result[j])
    
    for j in range(3):
        max_result[j] = max_tmp[j]
        min_result[j] = min_tmp[j]
   
print(max(max_result), min(min_result))