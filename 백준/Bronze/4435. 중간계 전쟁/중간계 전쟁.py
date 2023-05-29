n = int(input())
간달프 = [1, 2, 3, 3, 4, 10]
사우론 = [1, 2, 2, 2, 3, 5, 10]

for i in range(n):
    간달프_점수 = sum([간달프[idx] * num for idx, num in enumerate(list(map(int, input().split())))])
    사우론_점수 = sum([사우론[idx] * num for idx, num in enumerate(list(map(int, input().split())))])
    
    if 간달프_점수 > 사우론_점수:
        print("Battle {0}: Good triumphs over Evil".format(i+1))
    elif 간달프_점수 < 사우론_점수:
        print("Battle {0}: Evil eradicates all trace of Good".format(i+1))
    else:
        print("Battle {0}: No victor on this battle field".format(i+1))