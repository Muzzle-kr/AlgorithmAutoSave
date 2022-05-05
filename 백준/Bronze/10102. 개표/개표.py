a = b = 0
N = int(input())
for i in input():
    if i == 'A':
        a += 1
    else: 
        b += 1

if a > b: 
    print('A')
elif a < b:
    print('B')
else:
    print("Tie")