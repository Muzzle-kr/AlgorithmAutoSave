def solution(routes):
    answer = []
    routes = sorted(routes, key=lambda x: (x[1], x[0]))
    camera = 0
    for start, end in routes:
        if camera == 0:
            camera = end
            continue

        if start > camera and end >= camera:
            answer.append(camera)
            camera = end
    
    if camera != 0:
        answer.append(camera)
        
    return len(answer)