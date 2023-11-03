n = int(input())
word = input()                # 후위표기식을 word에 저장함
num_lst = [0] * n				  # 피연산자값을 저장하기 위한 num_lst 생성	

for i in range(n):
    num_lst[i] = int(input())  # 피연산자값 받기

stack = []                    # stack 리스트를 통해 후위표기식 계산

for i in word :					
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i)-ord('A')])
    else :						
        str2 = stack.pop()
        str1 = stack.pop()

        if i =='+' :
            stack.append(str1+str2)
        elif i == '-' :
            stack.append(str1-str2)
        elif i == '*' :
            stack.append(str1*str2)
        elif i == '/' :
            stack.append(str1/str2)

print('%.2f' %stack[0])