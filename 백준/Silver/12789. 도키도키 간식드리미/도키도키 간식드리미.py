n = int(input())
queue = list(map(int, input().split()))
stack = []
current_order = 1
# Queue에서 하나씩 꺼내서 순서에 맞는 지 체크
# 순서에 맞으면 current_order += 1
# Queue에서 꺼낸 값이 순서에 맞지 않으면 Stack에 넣음
# Stack에 넣은 값이 순서에 맞으면 current_order += 1

while queue or stack:
    if stack:
        s = stack.pop()
        
        if s == current_order:
            current_order += 1
            continue
        else:
            if not queue:
                break
            stack.append(s)
            
    if queue:
        q = queue.pop(0)
        
        # 순서가 맞으면 다음 순서로 넘김
        if q == current_order:
            current_order += 1
            continue
        else:
            stack.append(q)
    
if current_order == n + 1:
    print('Nice')
else:
    print('Sad')