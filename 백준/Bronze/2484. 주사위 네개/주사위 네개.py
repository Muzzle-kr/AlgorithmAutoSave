import sys
input = sys.stdin.readline

prize = []
for _ in range(int(input())):
    dices = list(map(int, input().split()))
    
    obj = {}
    
    for d in dices:
        if d in obj:
            obj[d] += 1
        else:
            obj[d] = 1
    # 배열을 list로 변환
    newObj = list(sorted(obj.items(), key=lambda x: x[1], reverse=True))
    
    # print("같은 눈이 4개 나온 경우")
    if len(obj) == 1:
        value = 50000 + (newObj[0][0] * 5000)
        prize.append(value)
        
    elif len(obj) == 2:
        # print("같은 눈이 2개씩 나온 경우")
        if newObj[0][1] == 2 and newObj[1][1] == 2:
            value = 2000 + (newObj[0][0] * 500) + (newObj[1][0] * 500)
            prize.append(value)
        # print("같은 눈이 3개, 1개씩 나온 경우")
        else:
            value = 10000 + (newObj[0][0] * 1000)
            prize.append(value)
    else:
        # print("같은 눈이 2개, 1개, 1개씩 나온 경우")
        if newObj[0][1] == 2:
            value = 1000 + (newObj[0][0] * 100)
            prize.append(value)
        else:
            # print("같은 눈이 1개씩 나온 경우")
            value = max(dices) * 100
            prize.append(value)
print(max(prize))