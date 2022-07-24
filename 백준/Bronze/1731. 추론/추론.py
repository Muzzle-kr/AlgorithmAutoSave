repeat = int(input())
base = int(input())
num_comparsion = int(input())
progression = 0;
num_calculate = 0;
last_num = 0;    

if num_comparsion % base == 0:
    progression = 1 # 등비수열
    num_calculate = num_comparsion // base
else:
    progression = 2 # 등차수열
    num_calculate = num_comparsion - base

for i in range(2, repeat):
    tmp = int(input())
    if i == repeat - 1:
        last_num = tmp
        
if progression == 1: # 등비수열 계산
    print(last_num * num_calculate)
else: # 등차수열 계산
    print(last_num + num_calculate)