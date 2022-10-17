N = int(input())
arr = list(map(int, input().split()))
rest = 0

for i in arr:
    result = sum(arr)
    
if result % 3 != 0:
    print("no")
else:
    print("yes")