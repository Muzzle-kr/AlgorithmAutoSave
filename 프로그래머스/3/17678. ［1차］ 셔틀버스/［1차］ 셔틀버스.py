from collections import deque

def convertToMin(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)

def convertToHHMM(min):
    hour = min // 60
    minute = min % 60
    return str(hour).zfill(2) + ':' + str(minute).zfill(2)

def solution(n, t, m, timetable):
    answer = ''
    # 줄을 선 시간 순으로 정렬
    timetable.sort()
    queue = deque(timetable)
    cur_bus_time = 540
    result = []
    
    # 버스 좌석에 태우기
    idx = 0
    while idx < n:
        tmp_seat = []
        
        while queue:
            time = queue.popleft()
            convertedMinTime = convertToMin(time)
            
            if cur_bus_time >= convertedMinTime:
                tmp_seat.append(time)
                if len(tmp_seat) == m:
                    break
            else:
                queue.appendleft(time)
                break
        result.append(tmp_seat)
        # 다음 버스를 부른다.
        idx += 1
        
        # 다음 버스 시간으로 변경
        if idx < n:
            cur_bus_time += t
        
    # 버스 좌석이 비어있는 경우: 해당 버스 출발 시간에 맞춰서 탄다.
    if len(result[n-1]) < m:
        answer = convertToHHMM(cur_bus_time)
    # 버스 좌석이 없는 경우: 마지막 사람보다 1분 일찍 온다.
    else:
        answer = convertToHHMM(convertToMin(result[n-1][-1]) - 1)
        
    return answer