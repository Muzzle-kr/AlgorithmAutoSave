
for i in range(int(input())):
    N, M = map(int, input().split())

    factMemo = [0, 1]
    # factorial memo 세팅
    for i in range(2, M + 1):
        factMemo.append(factMemo[i-1] * i)
    
    if N == M:
        print(1)
    
    else:
        print(int(factMemo[M] // factMemo[N] // factMemo[M-N]))