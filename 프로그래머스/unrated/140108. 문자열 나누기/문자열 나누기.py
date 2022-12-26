def solution(s):
    answer = 0
    equalCount = 0
    nonEqualCount = 0
    x = ""
    
    # while True:
    #     if len(s) == 1 or s == "":
    #         break
    #     print(f"문장은 {s} 입니다.")
        
    for idx, w in enumerate(s):
        
        if x == "":
            # print(f'idx는 0입니다. 시작 문자는 {w}입니다.')
            x = w
            equalCount += 1
            continue  
        if w == x:
            equalCount += 1
        else:
            nonEqualCount += 1
        
        if equalCount == nonEqualCount:
            # print(f"분해된 문장: {s[:idx+1]}, idx : {idx}")
            answer += 1
            x = ""
            equalCount = 0
            nonEqualCount = 0
            # print(f"수정된 문장: {s}, idx : {idx}")
            # break

    if x != "":
        answer += 1
    # print(x)
    return answer