from bisect import bisect_left

def solve(smaller, bigger):
    global result
    small_idx = 0
    bigger_idx = len(bigger) - 1
    
    while small_idx < len(smaller) and bigger_idx >= 0:
        if smaller[small_idx] + bigger[bigger_idx] < 0:
            result += 1
            small_idx += 1
            bigger_idx -= 1
        else:
            bigger_idx -= 1
    
N = int(input())
M = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

result = 0

m_plus_idx = bisect_left(M, 0)
w_plus_idx = bisect_left(W, 0)

solve(M[:m_plus_idx], W[w_plus_idx:])
solve(W[:w_plus_idx], M[m_plus_idx:])

print(result)