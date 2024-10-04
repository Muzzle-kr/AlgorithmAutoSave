S = int(input())
total = 0

for i in range(4_294_967_296):
    total += i
    
    if total > S:
        print(i-1)
        break