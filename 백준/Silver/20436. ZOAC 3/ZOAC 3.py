left_alpha = 'qwertasdfgzxcv'

qwerty_alpha = [
    'qwertyuiop','asdfghjkl','zxcvbnm'
]


# 초기 세팅 구하기
def find_coordinates(s):    
    x, y = "", ""
    for i in range(3):
        if s in qwerty_alpha[i]:
            x = i
            y = qwerty_alpha[i].index(s)
    return [x, y]



def cal_coordinates(x1, y1, x2, y2):
    result = abs(x1-x2) + abs(y1-y2)
    return abs(x1-x2) + abs(y1-y2)

left, right = input().split()
sentence = input()
left_x, left_y = find_coordinates(left)
right_x, right_y = find_coordinates(right)
ans = 0

for s in sentence:
    x, y = find_coordinates(s)
    
    if s in left_alpha:
        ans += cal_coordinates(left_x, left_y, x, y)            
        left_x = x
        left_y = y
    else:
        ans += cal_coordinates(right_x, right_y, x, y)            
        right_x = x
        right_y = y

print(ans+len(sentence))