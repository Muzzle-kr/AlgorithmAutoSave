for i in range(int(input())):
    arr = list(map(int, input().split()))
    score = arr[1:]
    score.sort(reverse=True)
    maxNum = score[0]
    minNum = score[-1]
    largestGap = 0
    
    for idx, j in enumerate(score):
        if idx != len(score) -1:
            gap = score[idx] - score[idx+1]

            if largestGap < gap:
                largestGap = gap
        
    print(f"Class {i + 1}")
    print(f'Max {maxNum}, Min {minNum}, Largest gap {largestGap}')