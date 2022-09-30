repeat = int(input())

target = 1
arr = []
comparisonArr = [0]

for _ in range(repeat):
    arr.append(int(input()))

idx = 0
result = []

while idx < len(arr):    
    # 입력받은 수열의 idx와 순차 수열의 마지막 값이 같다면 result값에 -를 push하고 순차수열에서 pop해준다!
    if arr[idx] == comparisonArr[-1]:
        result.append('-')
        comparisonArr.pop()
        idx += 1    
    # 입력받은 수열의 idx가 순차 수열의 마지막 값보다 크다면 result값에 +를 push하고 N을 순차수열에다가 더해준다
    elif arr[idx] > comparisonArr[-1]:
        result.append('+')
        comparisonArr.append(target)
        target += 1
    else:
        if len(comparisonArr) > 1:
            break
        else:
            continue

if len(comparisonArr) == 1:
    for i in result:
        print(i)
else:
    print("NO")


