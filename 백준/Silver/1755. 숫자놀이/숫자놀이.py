dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6:  "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

def solution():
    n, m = map(int, input().split())
    
    def converter(i):
        return ''.join([dict[int(j)] for j in str(i)])
    
    sorted_arr = sorted([(converter(i), i) for i in range(n, m+1)], key=lambda x: x[0])
    
    
    idx = 0
    while idx < len(sorted_arr):
        print(*[i[1] for i in sorted_arr[idx:idx+10]])
        idx += 10
        
solution()