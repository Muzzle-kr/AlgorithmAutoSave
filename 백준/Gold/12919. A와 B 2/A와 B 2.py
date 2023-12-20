S = list(input())
T = list(input())

def dfs(t):
    if t == S:
        print(1)
        exit()
    
    if len(t) == 0:
        return
    
    if t[-1] == 'A':
        dfs(t[:-1])
    
    if t[0] == 'B':
        dfs(t[1:][::-1])
    
dfs(T)
print(0)