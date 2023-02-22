def solution(data, col, row_begin, row_end):
    answer = 0
    # 1. 정렬하기
    sortedData = sorted(data, key= lambda x: (x[col-1], -x[0]))
    
    
    for i in range(row_begin - 1, row_end):    
        # 2. mod 합
        total = 0
        for j in sortedData[i]:
            total += j % (i + 1)
        
        # 3. XOR
        answer = answer ^ total

    return answer