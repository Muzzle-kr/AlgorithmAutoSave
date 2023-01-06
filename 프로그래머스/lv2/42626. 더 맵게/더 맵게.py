import heapq as hq

def solution(scoville, K):
    answer = 0

    hq.heapify(scoville)
    h = []
    count = 0

    while scoville:

        if scoville[0] >= K and not h:
            return count
        h.append(hq.heappop(scoville))

        if len(h) == 2:
            count += 1
            total = h[0] + h[1] * 2

            h = []
            hq.heappush(scoville, total)


    return -1