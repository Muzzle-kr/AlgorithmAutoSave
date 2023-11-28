n, p = map(int, input().split())
word = input()
a, c, g, t = list(map(int, input().split()))


def check(word):
    a_cnt = word.count('A')
    c_cnt = word.count('C')
    g_cnt = word.count('G')
    t_cnt = word.count('T')
    
    return [a_cnt, c_cnt, g_cnt, t_cnt]

temp = check(word[:p])
answer = 0

if temp[0] >= a and temp[1] >= c and temp[2] >= g and temp[3] >= t:
    answer = 1
    
for i in range(1, n-p+1):
    if word[i-1] == 'A':
        temp[0] -= 1
    elif word[i-1] == 'C':
        temp[1] -= 1
    elif word[i-1] == 'G':
        temp[2] -= 1
    elif word[i-1] == 'T':
        temp[3] -= 1
        
    
    if word[i+p-1] == 'A':
        temp[0] += 1
    elif word[i+p-1] == 'C':
        temp[1] += 1
    elif word[i+p-1] == 'G':
        temp[2] += 1
    elif word[i+p-1] == 'T':
        temp[3] += 1
    
    if temp[0] >= a and temp[1] >= c and temp[2] >= g and temp[3] >= t:
        answer += 1
            
print(answer)


