def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * columns + j + 1
    
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        tmp = matrix[x1][y1]
        minimum = tmp

        # x+1을 tmp로 넣고 x+1에 x를 넣고 skip
        for k in range(x1, x2):
            tv = matrix[k+1][y1]
            matrix[k][y1] = tv
            minimum = min(minimum, tv)

        for k in range(y1, y2):
            tv = matrix[x2][k+1]
            matrix[x2][k] = tv
            minimum = min(minimum, tv)
            
        for k in range(x2, x1, -1):
            tv = matrix[k-1][y2]
            matrix[k][y2] = tv
            minimum = min(minimum, tv)
        
        for i in range(y2, y1, -1):
            tv = matrix[x1][i-1]
            matrix[x1][i] = tv
            minimum = min(minimum, tv)
        
        matrix[x1][y1+1] = tmp
        answer.append(minimum)

    return answer