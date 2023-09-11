from collections import Counter
N = int(input())
word = input()
word_component = Counter(word)
ans = 0

for _ in range(N-1):
    other_word = input()
    other_word_component = Counter(other_word)
    other_word_component.subtract(word_component)
    
    # 크기가 1 이상 차이나면 무조건 실패
    if abs(len(word) - len(other_word)) > 1:
        continue
    
    # 크기가 같으면 합이 0 또는 2면 성공
    if abs(len(word) - len(other_word)) == 0:
        result = sum([abs(i) for i in other_word_component.values()])
        if result == 2 or result == 0:
            ans += 1
    # 크기가 다르면 합이 1이면 성공
    else:
        result = sum([abs(i) for i in other_word_component.values()])
        if result == 1:
            ans += 1
print(ans)