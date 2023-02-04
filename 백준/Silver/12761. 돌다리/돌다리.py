import sys
from collections import deque
input = sys.stdin.readline

A, B, N, M = map(int, input().split())

q = deque()
q.append(N)

casesOfMove = [
  ["+", 1], 
  ["-", 1], 
  ["+", A], 
  ["-", A], 
  ["+", B], 
  ["-", B],
  ["*", A],
  ["*", B],
]

num = [0] * 100002
limit = 100000
isBreak = False

while q:
      position = q.popleft()

      for i in range(8):
          if casesOfMove[i][0] == "+":
              calculated = position + casesOfMove[i][1]  
              if 0 <= calculated <= limit and num[calculated] == 0:
                  if calculated == M:
                      num[M] = num[position] + 1
                      break
                  q.append(position + casesOfMove[i][1])
                  num[position + casesOfMove[i][1]] = num[position] + 1
                  
          elif casesOfMove[i][0] == "-":
              calculated = position - casesOfMove[i][1]  
              if 0<= calculated <= limit and num[calculated] == 0:
                  q.append(calculated)
                  num[calculated] = num[position] + 1
                  
          else:
              calculated = position * casesOfMove[i][1]
              if 0 <= calculated <= limit and num[calculated] == 0:
                  q.append(calculated)
                  num[calculated] = num[position] + 1
          
      if isBreak:
        break
  
print(num[M])