# 0은 앞에 있는 걸 지우고 1은 뒤에있는 걸 지우기
from collections import Counter
S = input()
s_cnt = Counter(S)
s_arr = list(S)

zero_cnt = 0
zero_idx = len(s_arr) - 1   
while zero_cnt < s_cnt['0'] // 2:
    if s_arr[zero_idx] == '0':
        s_arr[zero_idx] = ''
        zero_cnt += 1
    zero_idx -= 1
        
one_cnt = 0
one_idx = 0
while one_cnt < s_cnt['1'] // 2:
    if s_arr[one_idx] == '1':
        s_arr[one_idx] = ''
        one_cnt += 1
    one_idx += 1

print(''.join(s_arr))