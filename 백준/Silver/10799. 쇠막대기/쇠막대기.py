left = []
cnt = 0
last_s = ""

for s in input():
    if last_s == "":
        last_s = s
        left.append(s)
        continue
    
    if last_s == "(":
        if s == "(":
            # (가 연속 2개 나왔을 경우 막대기 추가
            left.append(s)
        else:
            cnt += len(left) - 1 # 레이저가 나오면 스택에 있는 막대기 수 +1만큼 더해줌
            left.pop()    
            
    elif last_s == ")":
        if s == "(":
            left.append(s)
        else:
            # 막대기가 닫힐 경우 막대기 하나 더해줌
            left.pop()
            cnt += 1
    last_s = s

print(cnt)