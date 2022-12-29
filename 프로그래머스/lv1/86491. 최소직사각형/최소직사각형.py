def solution(sizes):
    width = 0
    height = 0
    
    for i in sizes:    
      # 세로가 큰 것들은 돌려본다
      if i[1] > i[0]:
        width = max(width, i[1])
        height = max(height, i[0])
      else:
        width = max(width, i[0])
        height = max(height, i[1])
      
    return width * height