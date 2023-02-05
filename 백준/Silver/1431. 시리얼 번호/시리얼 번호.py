import re
arr = []
for i in range(int(input())):
    arr.append(input())
    
arr = sorted(arr, key=lambda x: (len(x), sum([int(i) for i in re.sub(r'[^0-9]', '', x)]), [ord(i) for i in x]))


for i in arr:
    print(i)