def solution(maps):
    height = len(maps)
    width = len(maps[0])
    start = [0, 0]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = [start]
    checkMaps = [[maps[y][i] for i in range(width)] for y in range(height)]
    
    checkMaps[0][0] = 1
    
    isFind = False
    
    while queue:
        y, x = queue.pop(0)
        
        
        for n in move:
            nx = x + n[1]
            ny = y + n[0]
            
            countOfBlock = 0
            
            if (nx < 0 or ny < 0 or nx >= width or ny >= height):
                countOfBlock += 1
                continue
            
            if checkMaps[ny][nx] == 0:
                countOfBlock += 1
                continue
            
            # 길을 찾았다!
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                checkMaps[ny][nx] = 0
            else:
                maps[ny][nx] = min(maps[y][x] + 1, maps[ny][nx])
            
            
            if countOfBlock == 4:
                print("여기옴?")
                return -1
            
            if ny == height-1 and nx == width-1:
                isFind = True
                break
            
            queue.append([ny, nx])
            
        
        # # 종료 조건
        # if maps[height-1][width-1] > 1:
        #     break
            
    # print(queue, x, y)
    if isFind:
        return maps[height-1][width-1]
    else:
        return -1