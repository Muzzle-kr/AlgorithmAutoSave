
result = [0]

N = int(input())
roads = list(map(int, input().split()))

heights = 0
tmp = []

# print(N, roads)

for idx, i in enumerate(roads):
    # print(f'i : {i}, tmp: {tmp}')
    if len(tmp) == 0:
        tmp.append(i)
    else:
        # 오르막길이라면
        if tmp[-1] < i:
            # print("오르막길입니다.")
            heights += (i - tmp[-1])
            result.append(heights)
            tmp.append(i)  
        # 내리막길 혹은 평지
        else:
            # print("내리막길 혹은 평지입니다.")
            heights = 0
            tmp = [i]

print(max(result))