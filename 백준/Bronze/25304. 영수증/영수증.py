totalPrice = int(input())
N = int(input())
sum = 0
for _ in range(N):
    price, amount = map(int, input().split())
    
    sum += price * amount
    
if totalPrice - sum == 0:
    print("Yes")
else:
    print("No")