def cleaning(original):
    original = str(original).zfill(4)
    
    if original[2] == "5":
        original = int(original) + 50
    else:
        original = int(original) + 10
    return original

def solution(book_time):
    answer = []
    book_time = [[int("".join(time.split(":"))) for time in book] for book in book_time]
    book_time.sort(key=lambda x: x[0])
    
    for idx, b in enumerate(book_time):
        if idx == 0:
            # print("첫번째방이기 때문이 집어넣음")
            answer.append([b])
            continue
        
        isReserved = False
        for idx, reservation in enumerate(answer):
            reservationCloseTime = reservation[-1][1]
                
            if cleaning(reservationCloseTime) <= b[0]:
                # print("방 새로 내줄 준비 되어있음")
                isReserved = True
                answer[idx].append(b)
                break
                
        if not isReserved:
            answer.append([b])
            
    return len(answer)
