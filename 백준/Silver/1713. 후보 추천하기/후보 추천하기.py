N = int(input())
M = int(input())
arr = list(map(int, input().split()))

dict = {}
photo = []

for i in range(M):
    # 후보가 사진틀에 없을 때
    if arr[i] not in dict:
        # 사진틀이 비어있을 때
        if len(photo) < N:
            photo.append(arr[i])
            dict[arr[i]] = [1, i]
        # 사진틀이 꽉 찼을 때
        
        else:
            idx = sorted(dict.items(), key=lambda x: (x[1][0], x[1][1]))[0][0]
            del dict[idx]
            photo.remove(idx)
            
            photo.append(arr[i])
            dict[arr[i]] = [1, i]
    # 이미 사진 틀에 있을 떄
    else:
        dict[arr[i]][0] += 1

print(*sorted(photo))