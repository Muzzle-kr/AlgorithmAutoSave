def solution(scores):
    answer = 1
    wanho = scores[0]
    sum_wanho = wanho[0] + wanho[1]
    # 근무평가 내림차순, 동료평가 오름차순
    scores.sort(key=lambda x:(-x[0], x[1]))
    max_score = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1

        # 동료평가 점수 최고점보다 높아야된다.
        if max_score <= score[1]:
            if sum_wanho < score[0] + score[1]:
                answer += 1
            max_score = score[1]
    return answer