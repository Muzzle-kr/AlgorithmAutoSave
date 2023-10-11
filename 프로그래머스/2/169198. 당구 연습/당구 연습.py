def solution(m, n, startX, startY, balls):
    answer = []
    for targetX, targetY in balls:
        candidate_x_down = (targetX - startX) ** 2 + (targetY + startY) ** 2
        candidate_x_up = (targetX - startX) ** 2 + (targetY - 2 * n + startY) ** 2
        candidate_y_left = (targetX + startX) ** 2 + (targetY - startY) ** 2
        candidate_y_right = (targetX - 2 * m + startX) ** 2 + (targetY - startY) ** 2

        if targetX == startX:
            if targetY > startY:
                answer.append(min(candidate_x_down, candidate_y_left, candidate_y_right))
            else:
                answer.append(min(candidate_x_up, candidate_y_left, candidate_y_right))
        elif targetY == startY:
            if targetX > startX:
                answer.append(min(candidate_x_down, candidate_x_up, candidate_y_left))
            else:
                answer.append(min(candidate_x_down, candidate_x_up, candidate_y_right))
        else:
            answer.append(min(candidate_x_down, candidate_x_up, candidate_y_left, candidate_y_right))
    return answer