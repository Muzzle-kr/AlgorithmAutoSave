import math

def solution(fees, records):
    carObj = {}
    result = []
    closeTime = 23 * 60 + 59
    basicTime, basicFee, unitTime, unitFee = fees
    # print(basicTime, basicFee, unitTime, unitFee)
    for i in records:
        time, carNumber, inOut = i.split()
        h, m = map(int, time.split(':'))
        
        if carNumber not in carObj:
            carObj[carNumber] = [h * 60 + m]
        else:
            carObj[carNumber].append(h * 60 + m)
    
    carObj = sorted(carObj.items(), key=lambda x: x[0])
    # print(carObj)
    for carInOutHistory in carObj:
        carNumber = carInOutHistory[0]
        usingTime = -basicTime
        enterTime = 0
        # 출차가 안됐다면
        for idx, time in enumerate(carInOutHistory[1]):
            # print(f'idx: {idx}, time: {time}, closeTime: {closeTime}, enterTime: {enterTime}, usingTime: {usingTime}')
            if idx % 2 == 0:
                if idx == len(carInOutHistory[1]) - 1:
                    usingTime += (closeTime - time) 
                else:
                    enterTime = time
            else:
                usingTime += (time - enterTime)
                # entertime 초기화
                enterTime = 0
        
        if usingTime > 0:
            result.append(basicFee + (math.ceil(usingTime / unitTime) * unitFee))
        else:
            result.append(basicFee)
        # print(f' carNumber: {carNumber}, usingTime: {usingTime}, result: {result}')
        

    return result