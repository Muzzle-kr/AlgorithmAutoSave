# 내림차순 정렬로 좋은 것들 순으로 묶어서 판매하기
def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    box = []
    for i in score:
        box.append(i)
        
        if len(box) == m:
            answer += min(box) * m # 가격매기기
            box = [] # 박스 초기화
    return answer