P, M = map(int, input().split())
rooms = []
        
def generateNewRoom(level, nickname):
    global rooms
    
    room = []
    min_level = level - 10
    max_level = level + 10
    
    room.append([min_level, max_level])
    room.append([level, nickname])
    rooms.append(room)
    
def printParticipants(room, isStart):
    if isStart:
        print("Started!")
    else:
        print("Waiting!")
    for level, nickname in sorted(room[1:], key=lambda x: x[1]):
        print(level, nickname)

        
isWaiting = True
for _ in range(P):
    level, nickname = input().split()
    level = int(level)
    
    # 새로운 방 생성
    if len(rooms) == 0:
        generateNewRoom(level, nickname)
    # 생성된 방을 돈다.
    else:
        
        for idx, room in enumerate(rooms):
            min_level = room[0][0]
            max_level = room[0][1]
            isFind = False
            
            # 레벨이 맞다면 방에 입장한다.
            if min_level <= level <= max_level and len(room) < M + 1:
                rooms[idx].append([level, nickname])
                isFind = True
                break
        
        # 맞는 방을 못찾았다면 새 방 만들기
        if not isFind:
            generateNewRoom(level, nickname)
            
for room in rooms:
    if len(room[1:]) == M:
        isWaiting = False
        printParticipants(room, True)
        continue
    else:
        printParticipants(room, False)