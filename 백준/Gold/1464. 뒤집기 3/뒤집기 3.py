import sys
input = sys.stdin.readline
word = list(input().rstrip())

def convert_string(S):
    return S[::-1]

for i in range(len(word)-1):
    if ord(word[i]) > ord(word[i+1]) and ord(word[0]) >= ord(word[i+1]):
        # 2번 뒤집기
        s1 = convert_string(word[:i+1])
        s2 = convert_string(s1 + [word[i+1]])
        
        # 단어 변경
        for i in range(len(s2)):
            word[i] = s2[i]
print(''.join(word))