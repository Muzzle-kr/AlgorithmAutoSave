import math
def solution(k, d):
    answer = 0
    yLimit = d * d
    for i in range(0, d + 1, k):
        xLimit = i * i
        res_d = math.floor(math.sqrt(yLimit-xLimit))
        answer += (res_d//k) + 1
    return answer

