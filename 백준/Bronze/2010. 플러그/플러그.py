repeat = int(input())

sum = 0
for i in range(repeat):
    num = int(input())
    
    if i == repeat -1:
        sum += num # 마지막은 제외하지 않음
    else:
        sum += num - 1 # 연결 할 때마다 1개씩 제외
    
print(sum)
    