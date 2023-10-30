K = int(input())
word = "A"
a_cnt = 1
b_cnt = 0

for i in range(1, K+1):
    tmp = a_cnt
    a_cnt = b_cnt
    b_cnt = b_cnt + tmp

print(a_cnt, b_cnt)