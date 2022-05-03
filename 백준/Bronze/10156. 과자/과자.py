price, num, money = map(int, input().split())

if price * num <= money:
    print(0)
else: 
    print(price * num - money)