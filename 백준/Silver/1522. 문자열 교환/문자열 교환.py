s = input()
a_cnt = s.count('a')
s += s[:a_cnt] # 원형처리

min_val = int(1e9)
for i in range(len(s)-a_cnt):
    min_val = min(min_val, s[i:i+a_cnt].count('b'))
    
print(min_val)