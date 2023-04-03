def solution(s):
    answer = 1
    # 큰 팰린드롬부터 찾아서 return
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if is_palindrome(s[i:j]):
                answer = max(answer, j-i)
    return answer
def is_palindrome(s):
    return s == s[::-1]