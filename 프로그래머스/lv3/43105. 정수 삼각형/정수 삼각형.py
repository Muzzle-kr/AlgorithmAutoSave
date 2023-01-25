# 나머지는 무시된다.
# 최소값이 8보다 크면 -1 반환
def solution(triangle):
    answer = [[0]*(i+1) for i in range(len(triangle))]
    answer[0] = triangle[0]
    
    # 겹치는 건 덮어쓰기
    for i in range(0, len(triangle) - 1):
        for idx, j in enumerate(answer[i]):
            answer[i + 1][idx] = max(answer[i + 1][idx], answer[i][idx] + triangle[i + 1][idx])
            answer[i + 1][idx + 1] = max(answer[i][idx] + triangle[i + 1][idx + 1], answer[i + 1][idx + 1])
        
    return max(answer[-1])