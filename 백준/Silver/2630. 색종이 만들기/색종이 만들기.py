n = int(input())
arr = []
answer = [0, 0]

for i in range(n):
    arr.append(list(map(int, input().split())))

def divideConquer(arr):
    if len(arr) == 1:
        answer[arr[0][0]] += 1
        return 
    
    mark = arr[0][0]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != mark:
                divideConquer([row[:len(arr)//2] for row in arr[:len(arr)//2]])
                divideConquer([row[:len(arr)//2] for row in arr[len(arr)//2:]])
                divideConquer([row[len(arr)//2:] for row in arr[:len(arr)//2]])
                divideConquer([row[len(arr)//2:] for row in arr[len(arr)//2:]])
                return
    
    answer[mark] += 1      
    return
    

divideConquer(arr)    
print(answer[0])
print(answer[1])