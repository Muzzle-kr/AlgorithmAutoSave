from collections import deque

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cacheList = deque([])
    answer = 0

    for i in cities:
        i = i.lower()
        if i in cacheList:
            # print(f'Filter 전 CacheList: {cacheList}')
            cacheList = deque(filter(lambda x: x != i, cacheList))
            # print(f'Filter 후 CacheList: {cacheList}')
            cacheList.append(i)
            answer += 1
        else:
            if len(cacheList) == cacheSize:
                # print(f'cacheList: {cacheList}')
                cacheList.popleft()
            cacheList.append(i)
            answer += 5
    return answer