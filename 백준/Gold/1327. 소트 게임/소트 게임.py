from collections import deque

N, K = map(int, input().split())
arr = list(map(str, input().split()))
correct_answer = "".join(sorted(arr))
visited_set = set()
visited_set.add("".join(arr))

q = deque()
q.append(("".join(arr), 0))

answer = -1
idx = 0
while q:
    word, cnt = q.popleft()
    
    # 오름차순 정렬된 나열이면 정답
    if word == correct_answer:
        answer = cnt
        break
    
    # 새로운 단어 복사
    
    for i in range(N-K+1):
        new_arr = list(word)
        temp_arr = new_arr[i:i+K]
        temp_arr.reverse()
        
        for j in range(K):
            new_arr[i+j] = temp_arr[j]
        
        new_word = "".join(new_arr)
        if new_word not in visited_set:
            visited_set.add(new_word)
            q.append((new_word, cnt+1))
        
print(answer)