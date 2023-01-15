from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    answer = 0
    length = 0    
    # 트럭 대기 줄이 끝날 때까지 반복 
    # bridge의 마지막에 트럭이 있을 경우 트럭을 빼주고 rotate 해준다.
    # 트럭 무게 합이 다리 무게 이하일 경우 트럭을 집어넣고 rotate 해준다.
    # rotate
    
    
    
    while truck_weights:
        if bridge_weight + truck_weights[0] <= weight and length < bridge_length:
            truck = truck_weights.pop(0)
            bridge[-1] = truck
            bridge_weight += truck
            length += 1

        if bridge[0] != 0:
            bridge_weight -= bridge[0]
            bridge[0] = 0
            length -= 1
        answer += 1
        # print(bridge, truck_weights, answer)
        
            
        bridge.rotate(-1)    
    
    for i in range(bridge_length - 1, 0, -1):
        if bridge[i] != 0:
            answer += i + 1
            break
        
    return answer + 1