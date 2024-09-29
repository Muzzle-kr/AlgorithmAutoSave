def consultation(days, earn, current_day):
    if current_day == n:
        earns.append(earn)
        return 
    
    
    consultation_days, consultation_earn = consultations[current_day]
    
    # 이미 상담을 진행 중이라면 다음 날로 넘기기
    if days > 0:    
        consultation(days-1, earn, current_day+1)
        return
    
    # 남은 날짜보다 상담시간이 길면 상담을 할 수 없다.
    if current_day + consultation_days > n:
        consultation(days-1, earn, current_day+1)
        return
    
    # 상담하기
    consultation(consultation_days-1, earn+consultation_earn, current_day+1)
    # 상담하지 않기
    consultation(days-1, earn, current_day+1)
    return
    
n = int(input())
consultations = [list(map(int, input().split())) for _ in range(n)]
earns = []

consultation(0, 0, 0)

print(max(earns))