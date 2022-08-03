import sys
input = sys.stdin.readline

T = int(input())
def search():
    N = int(input())
    notebook1 = list(map(int, input().split()))
    M = int(input())
    notebook2 = list(map(int, input().split()))
    notebook1.sort()

    for value in notebook2:    
        lt = 0 
        rt = len(notebook1) - 1
        count = 0
        
        while lt <= rt:
            mid = int((lt + rt) / 2)
            
            # print(f' lt = {lt}, rt = {rt}, mid = {mid}, notebook1[mid] = {notebook1[mid]}')
            isFound = False
            if notebook1[mid] == value:
                isFound = True
                break
            elif notebook1[mid] > value:
                rt = mid - 1
            else:
                lt = mid + 1
        
        if isFound:
            print(1)
        else:
            print(0)

for _ in range(T):
    search()