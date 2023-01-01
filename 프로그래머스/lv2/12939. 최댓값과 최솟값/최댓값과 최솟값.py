def solution(s):
    answer = sorted([int(i) for i in s.split()])
    answer = " ".join([str(answer[0]), str(answer[-1])])
    return answer