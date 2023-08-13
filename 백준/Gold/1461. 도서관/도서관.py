import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

plus_book = []
minus_book = []
max_book = 0

for i in range(N):
    if arr[i] > 0:
        plus_book.append(arr[i])
    else:
        minus_book.append(abs(arr[i]))
        
    if abs(arr[i]) > abs(max_book):
        max_book = abs(arr[i])
        
plus_book.sort(reverse=True)
minus_book.sort(reverse=True)

result = 0

for i in range(0, len(plus_book), M):
    if plus_book[i] != max_book:
        result += plus_book[i]
    
for i in range(0, len(minus_book), M):
    if minus_book[i] != max_book:
        result += minus_book[i]
        

result *= 2
result += abs(max_book)
print(result)
    
    