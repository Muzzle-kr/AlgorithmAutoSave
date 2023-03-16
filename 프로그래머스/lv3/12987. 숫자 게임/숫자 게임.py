import bisect

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    # 이분검색으로 큰 값 중 가장 작은 것을 찾고
    # 없다면 [0]부터 사용한다.
    # visit도 써야함
    visit = [0] * len(A)
    
    for i in range(len(A)):
        bi = bisect.bisect_left(B, A[i])
        
        # print(f'bi: {bi}, B:{B}, A:{A}')
        n = 0
        while n + bi < len(B):
            if visit[bi+n] == 0 and A[i] < B[n+bi]:
                # print(f'{A[i]}보다 큰 수는 {n+bi} 번쨰 {B[n+bi]}입니다.')
                B.pop(bi+n)
                visit.pop(bi+n)
                # print(B, visit)
                # visit[bi+n] = 1
                answer += 1
                break
            n += 1
            
    return answer