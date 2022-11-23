import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

while True:
    seq1 = list(map(int, input().split()))
    if sum(seq1) == 0:
        break

    seq1_length = seq1[0]
    seq1 = seq1[1:]
    
    seq2 = list(map(int, input().split()))
    seq2_length = seq2[0]
    seq2 = seq2[1:]
    
    total = 0
    seq1_idx = 0
    seq2_idx = 0
    
    for num in seq1:
        if bisect_right(seq2, num) - bisect_left(seq2, num) > 0:
            # 겹치는 값까지 더해줘야하기에 bisect_right 사용 (제외한다면 left)
            sum_seq1 = sum(seq1[seq1_idx:bisect_right(seq1, num)])
            sum_seq2 = sum(seq2[seq2_idx:bisect_right(seq2, num)])
            
            # 합계 중 큰 값을 total에 더해준다
            total += max(sum_seq1, sum_seq2)
            
            # 각 수열의 index 갱신
            seq1_idx = bisect_right(seq1, num)
            seq2_idx = bisect_right(seq2, num)
            
    total += max(sum(seq1[seq1_idx:]), sum(seq2[seq2_idx:]))
    print(total)
                        
            