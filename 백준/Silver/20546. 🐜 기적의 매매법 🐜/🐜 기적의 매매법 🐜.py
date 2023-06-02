initial_asset = int(input())
stocks = list(map(int, input().split()))

a_asset, b_asset = initial_asset, initial_asset
a_stock, b_stock = 0, 0

result = ""
rising_count, drop_count = 0, 0

for idx, stock in enumerate(stocks):
    
    # print(f'{idx+1}차의 주식 가격은 {stock}입니다.')
    if idx == 13:
        a_result = a_asset + a_stock * stock
        b_result = b_asset + b_stock * stock
        
        # print(f'마지막 날입니다. 준현이(A)의 총 자산은 : {a_result}입니다. 성민이의 총 자산은 : {b_result}입니다.')
        if a_result > b_result:
            print("BNP")
        elif a_result < b_result:
            print("TIMING")
        else:
            print("SAMESAME")
        break
    
    # a의 전략 무조건 사기
    if a_asset >= stock:
        # print(f'------------------준현이의 주식 상황-------------------------')
        # print(f'{idx+1}일 BNP전략으로 가능한 매도합니다.')
        a_stock += a_asset // stock
        a_asset %= stock
        
        # print(f'거래 결과: a_stock: {a_stock}, 남은 자산: a_asset: {a_asset}')
    
    if idx > 0:
        if stocks[idx] > stocks[idx-1]:
            # print(f'{idx+1}일차의 주식 가격 {stock}은 전날보다 상승하였습니다.')
            rising_count += 1
            drop_count = 0
        elif stocks[idx] < stocks[idx-1]:
            # print(f'{idx+1}일차의 주식 가격 {stock}은 전날보다 하락하였습니다.')
            rising_count = 0
            drop_count += 1
            
        # 3일 연속 상승장일 때 전량 매도
        if rising_count == 3:
            # print(f'------------------성민이의 주식 상황-------------------------')
            # print(f'{idx+1}일 차에 전량 매도합니다.')
            b_asset += b_stock * stock
            b_stock = 0
            # print(f'거래 결과: b_stock: {b_stock}, 남은 자산: b_asset: {b_asset}')
        # 3일 연속 하락장일 때 전량 매수
        if drop_count == 3:
            # print(f'------------------성민이의 주식 상황-------------------------')
            # print(f'{idx+1}일 차에 전량 매수합니다.')
            b_stock += b_asset // stock
            b_asset %= stock