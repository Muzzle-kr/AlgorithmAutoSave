import sys
input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = []

for _ in range(int(input())):
    order = list(input().rstrip())
    
    if order[0] == "L":
        if str1:
            str2.append(str1.pop())
            
    elif order[0] == "D":
        if str2:
            str1.append(str2.pop())
            
    elif order[0] == "B":
        if str1:
            str1.pop()
            
    else:
        str1.append(order[2])

str1.extend(reversed(str2))
print(''.join(str1))