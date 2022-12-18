result = [0]

N = int(input())
roads = list(map(int, input().split()))

heights = 0
tmp = []

for i in roads:
    if len(tmp) == 0:
        tmp.append(i)
    else:
        # 오르막길이라면
        if tmp[-1] < i:
            heights += (i - tmp[-1])
            result.append(heights)
            tmp.append(i)  
        # 내리막길 혹은 평지
        else:
            heights = 0
            tmp = [i]

print(max(result))