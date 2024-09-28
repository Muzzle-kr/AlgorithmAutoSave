# 문제 4. 숫자야구 ( # 2503 )
 
# A는 3자리 숫자로 된 정답을 하나 정합니다.
 
# B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 합니다.
 
# B가 말한 숫자가 정답에 포함되어 있다면 1 Ball입니다.
# B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1 Strike입니다.

# 다른 숫자로 이루어진 세 자리수
 
# Strike와 Ball의 결과를 보고, 가능한 숫자를 계산하는 프로그램을 작성하세요.
 
# 4
# 123 1 1
# 356 1 0
# 327 2 0
# 489 0 1
 
# 2



# 
N = int(input())
hints = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i != j and j != k and k != i:                
                candidates = str(i) + str(j) + str(k)
                is_possible = True
                
                for hint in hints:
                    strike, ball = 0, 0
                    number, s, b = hint
                    number_str = str(number)
                    
                    # Strike // Ball 판단
                    
                    for x in range(3):
                        if candidates[x] == number_str[x]:
                            strike += 1
                    
                    for x in range(3):
                        if candidates[x] != number_str[x] and candidates[x] in number_str:
                            ball += 1
                    
                        
                    # 하나라도 맞지 않으면 다음 숫자로 넘어가기
                    if strike != s or ball != b:
                        is_possible = False
                        break
                
                if is_possible:
                    answer += 1
print(answer)
                