n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[i, set()] for i in range(n+1)]

for s_idx in range(n):
    for g in range(5):
        s_class = arr[s_idx][g]
        
        for ds_idx in range(n):
            if s_idx == ds_idx:
                continue
            
            if s_class == arr[ds_idx][g]:
                result[s_idx][1].add(ds_idx)
                
result.sort(key=lambda x: (-len(x[1]), x[0]))
print(result[0][0]+1)