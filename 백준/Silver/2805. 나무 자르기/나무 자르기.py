N, M = map(int, input().split())
trees = list(map(int, input().split()))


left = 0
right = max(trees)
answer = 0

while left <= right:
    saw_blood = (left + right) // 2
    total = 0

    
    for height in trees:
        total += max(0, height - saw_blood)
    
    # 필요한만큼 나무를 취했다면 정답을 최신화
    if total >= M:
        answer = saw_blood
        left = saw_blood + 1
    else:
        right = saw_blood - 1

print(answer)