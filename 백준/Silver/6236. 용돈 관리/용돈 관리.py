N, M = map(int, input().split())
spend_money = [int(input()) for _ in range(N)]

left = min(spend_money)
right = sum(spend_money)
result = 0
    
while left <= right:
    mid = (left + right) // 2
    
    current_money = mid
    cnt_withdrawal = 1
    
    for daily_spending in spend_money:
        if current_money < daily_spending:
            cnt_withdrawal += 1
            current_money = mid
        current_money -= daily_spending
    
    if cnt_withdrawal > M or mid < max(spend_money):
        left = mid + 1
    else:
        right = mid - 1
        result = mid
        
print(result)
        