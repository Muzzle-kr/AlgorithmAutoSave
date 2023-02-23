from collections import defaultdict
def solution(want, number, discount):
    # 10일동안 회원자격 부여, 15일동안 discount
    # discount를 돌면서 want에 있는지 확인
    # 있으면 number에서 빼기
    # 10일 기준으로 작업 
    # number의 합이 0이 되면 answer += 1
    # sales가 0이 되면 기존값 다시 다 더하기
    
    # sales = defaultdict(int)
    answer = 0
    
    need = number[:]
    
    # print(f'need: {need}, want:{want}')
    for i, dis in enumerate(discount):
        
        if i >= 10:
            pastSaleItem = discount[i-10]
            # sales[pastSaleItem] -= 1
            
            # 과거 세일 품목이 0이면 기존에 샀던 것 다시 원복시키기
            if pastSaleItem in want:
                need[want.index(pastSaleItem)] += 1
                
        # print(f'----------------------')  
        # print(f'{i+1}일차에 할인품목::: {dis}')
        if dis in want:
            # print(f'{i+1}일차에 {dis} 구매, {want.index(dis)}번째 품목')
            need[want.index(dis)] -= 1
        
        # print(f'{i+1}일차에 장보고 남은 것 {need}')     
        if ([max(i, 0) for i in need if i <= 0 ]).count(0) == len(need):
            # print(f'{i-9}일차에 할인행사 가능')
            answer += 1
            
            
        
    return answer