def solution(arr):
    previous = ""
    answer = []
    for i in arr:
        if i != previous:
            answer.append(i)
            previous = i
    return answer