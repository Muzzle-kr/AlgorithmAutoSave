import copy

for _ in range(int(input())):
    floor = int(input())
    number = int(input())
    
    lowerFloor = [0 for _ in range(number)]
    nowFloor = [0 for _ in range(number)]
    
    for i in range(floor + 1):
        for j in range(number):
            if i == 0:
                lowerFloor[j] = j + 1
            else:
                # print(f'아래층 상황 : {lowerFloor}')
                # print(f'현재 층은 {i} 층, 호수는 {j+1}호입니다.')    
                nowFloor[j] = sum(lowerFloor[:j+1])
                # print(f'바뀐  nowFloor : {nowFloor}')
        if i != 0:
            lowerFloor = copy.deepcopy(nowFloor)
            
    print(nowFloor[number - 1])
            
            
            
                