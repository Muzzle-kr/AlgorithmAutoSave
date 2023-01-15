from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights
    bridge = deque([0] * bridge_length)
    bridge_weight = 0
    answer = 0
    length = 0    
    
    while truck_weights:
        answer += 1
        bridge.rotate(-1)    
        if bridge_weight + truck_weights[0] <= weight and length < bridge_length:
            truck = truck_weights.pop(0)
            bridge[-1] = truck
            bridge_weight += truck
            length += 1

        if bridge[0] != 0:
            bridge_weight -= bridge[0]
            bridge[0] = 0
            length -= 1
    
    for i in range(bridge_length - 1, 0, -1):
        if bridge[i] != 0:
            answer += i + 1
            break
        
    return answer