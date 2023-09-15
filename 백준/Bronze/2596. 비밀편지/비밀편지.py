my_dict = {
    '000000': "A",
    "001111": "B",
    "010011": "C",
    "011100": "D",
    "100110": "E",
    "101001": "F",
    "110101": "G",
    "111010": "H"
}

N = int(input())
arr = list(input())
ans = ""

def checkWordInDict(word):
    for i in range(6):
        a = '1' if word[i] == '0' else '0'  # '0'과 '1'로 비교
        newWord = word[:i] + a + word[i+1:]
        if newWord in my_dict:
            return my_dict[newWord]
    return ""

for i in range(0, N*6, 6):  # 시작값을 0으로 변경
    word = ''.join(arr[i:i+6])  # 인덱스 범위를 수정
    if word in my_dict:
        ans += my_dict[word]
    else:
        newWord = checkWordInDict(word)
        if newWord != "":
            ans += newWord
        else:
            ans = str(i//6+1)  # 숫자를 문자열로 변환
            break

print(ans)
