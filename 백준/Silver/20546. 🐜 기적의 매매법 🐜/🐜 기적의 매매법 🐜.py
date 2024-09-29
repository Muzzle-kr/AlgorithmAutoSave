money = int(input())
stocks = list(map(int, input().split()))
jh_money = money
jh_stocks = 0
sm_money = money
sm_stocks = 0

increase_days = 0
decrease_days = 0
before_stock = 0

for day, stock in enumerate(stocks):
    
    # 상승장 or 하락장
    if before_stock > stock:
        decrease_days += 1
        increase_days = 0
    elif stock < before_stock:
        increase_days += 1
        decrease_days = 0
    else:
        increase_days = 0
        decrease_days = 0
        
    before_stock = stock
    
    
    # 상승장이 3일 이상일 경우 전량 매도
    if increase_days >= 3 and sm_stocks:
        sm_money = sm_stocks * stock
        sm_stocks = 0
        
    # 하락장이 3일 이상일 경우 전량 매수
    if decrease_days >= 3 and sm_money >= stock:
        sm_stocks = sm_money // stock
        sm_money = sm_money % stock
        
        
    # 준현이는 살 수 있으면 무조건 구매
    if jh_money >= stock:
        jh_stocks = jh_money // stock
        jh_money = jh_money % stock
    
    
    # 마지막 날일 때 비교
    if day == 13:
        jh_result = jh_money + jh_stocks * stock
        sm_result = sm_money + sm_stocks * stock

        # print(f'jh_money: {jh_money}, jh_stocks: {jh_stocks}')
        # print(f'sm_money: {sm_money}, sm_stocks: {sm_stocks}')
        if jh_result > sm_result:
            print("BNP")
        elif jh_result < sm_result:
            print("TIMING")
        else:
            print("SAMESAME")