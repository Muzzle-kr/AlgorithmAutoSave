def solution(numbers):
    answer = []
    
    bigNumber = []
    
    for i in range(len(numbers)-1, -1, -1):
        if i == len(numbers)-1:
            bigNumber.append(numbers[i])
            answer.append(-1)
        else: 
            count = 1
            isFind = False
            while count < len(bigNumber) + 1:
                # print(f'bigNumber: {bigNumber}, count: {count}, i: {i}, numbers[i]: {numbers[i]}')
                if numbers[i] < bigNumber[-count]:
                    answer.append(bigNumber[-count])
                    bigNumber.append(numbers[i])
                    isFind = True
                    break
                count += 1
            if not isFind:
                bigNumber.append(numbers[i])
                answer.append(-1)

    return answer[::-1]