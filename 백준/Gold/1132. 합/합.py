N = int(input())

alphabet_dict = {
    "A": [0, False],
    "B": [0, False],
    "C": [0, False],
    "D": [0, False],
    "E": [0, False],
    "F": [0, False],
    "G": [0, False],
    "H": [0, False],
    "I": [0, False],
    "J": [0, False],
}

for _ in range(N):
    word = input()
    
    # 첫 글자 확인
    alphabet_dict[word[0]][1] = True
    n = 1
    
    for i in range(len(word)-1, -1, -1):
        alphabet_dict[word[i]][0] += n
        n *= 10

alphabet_sorted_arr = sorted(alphabet_dict.items(), key=lambda x: x[1][0], reverse=True)

# 0에 해당하는 숫자가 첫글자로 있을 경우 다음 첫 숫자가 아닌 숫자를 삭제함
if alphabet_sorted_arr[9][1][1]:
    for i in range(8, -1, -1):
        if not alphabet_sorted_arr[i][1][1]:
            alphabet_sorted_arr.pop(i)
            break
ans = 0

for i in range(9):
    ans += alphabet_sorted_arr[i][1][0] * (9-i)
    
print(ans)
