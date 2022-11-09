# 1순위: 5로만 나눠지는 것
# 2순위: 5와 3이 섞인 것
# 3순위: 3으로 나눠지는 것
N = int(input())

count = 0
repeat = 1
multipleOfThree = 0

while (N != 0 and multipleOfThree <= N):
    multipleOfThree = repeat * 3
    
    # print(f'repeat: {repeat} multipleOfThree: {multipleOfThree}, N: {N}')
    if (N % 5 == 0):
        print(N // 5)
        exit()
        
    if ((N - multipleOfThree) % 5 == 0 and (N - multipleOfThree) > 0):
        share = (N - multipleOfThree) // 5
        # print(f"5나누기 3kg {repeat}개 사용, 5kg {share}개 사용")
        N = 0
        count = repeat + share
        break
    
    if (multipleOfThree >= N and N % 3 == 0):
        # print("3나누기")
        share = N // 3
        N = 0
        count = share
        break

    if ((repeat * 3) > N):
        print(-1)
        exit()
        
    repeat += 1


print(count)
