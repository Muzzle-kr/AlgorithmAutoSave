import sys
input = sys.stdin.readline

def solution(word, start):
    if not word:
        return
    
    target = min(word)
    idx = word.index(target)
    
    ans[start+idx] = target
    
    print("".join(ans))

    
    # 뒷 배열 확인
    solution(word[idx+1:], start+idx+1)
    # 앞 배열 확인
    solution(word[:idx], start)

word = input().rstrip()
ans = [""] * len(word)
word_arr = list(word)
solution(word_arr, 0)