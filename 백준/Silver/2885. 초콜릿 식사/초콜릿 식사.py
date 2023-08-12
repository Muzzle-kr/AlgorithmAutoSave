import sys
input = sys.stdin.readline

K = int(input())

size = 1
count = 0

while size < K:
    size = size << 1
    
result = size

while K > 0:
    if K >= size:
        K -= size
    else:
        size //= 2
        count += 1
        
print(result, count)