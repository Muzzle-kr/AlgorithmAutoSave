R, C, ZR, ZC = map(int, input().split())

arr = []
result = []
for i in range(R):
    arr.append(list(input()))

for i in range(R):
    tmpArr = []
    
    for j in arr[i]:
        # ZC를 곱해서 tmpArr에 저장
        tmpArr.append(j * ZC)
    
    # ZR만큼 반복하면서 result에 저장
    for _ in range(ZR):
        result.append(tmpArr)
    

for i in range(R*ZR):
    print("".join(result[i]))