def solution(price, money, count):
    print(price, money, count)
    n = 1
    while count:
        print(f'money: {money}')
        money -= (price * n)
        n += 1
        count -= 1
    if money < 0:
        return abs(money)
    else:
        return 0