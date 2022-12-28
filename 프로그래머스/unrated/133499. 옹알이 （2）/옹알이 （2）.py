def solution(babbling):
    answer = 0
    pronounce = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        print(bab)
        for p in pronounce:
            if p * 2 not in bab:
                bab = bab.replace(p, "1")
        try: 
            print(bab)
            num = int(bab)
            answer += 1
        except:
            continue
    return answer