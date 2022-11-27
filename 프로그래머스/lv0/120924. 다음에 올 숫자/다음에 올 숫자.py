def solution(common):
    if (common[2] - common[1]) == (common[1] - common[0]):
        num = common[2] - common[1]
        return int(common[-1] + num)
    else:
        num = common[2] / common[1]
        return int(common[-1] * num)