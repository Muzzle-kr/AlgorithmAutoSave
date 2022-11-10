result = 0
for i in range(1, int(input()) + 1):
  if len(str(i)) < 3:
    result += 1
  else:
    strNum = str(i)
    equalDifference = -1001
    lastNum = 0
    count = 0
    # 자릿수 반복
    for idx, j in enumerate(strNum):
      # idx가 0일 경우
      if idx == 0:
        # lastNum을 strNum[0]으로 치환
        lastNum = int(j)
      # idx가 1 이상일 경우
      else:
        if equalDifference != -1001:
            if equalDifference == lastNum - int(j):
              # 등차수열일 경우 count
              count += 1
              lastNum = int(j)
            else:
              # 등차수열이 아닐 경우
              equalDifference = lastNum - int(j)
              lastNum = int(j)
        else:
          # 등차수열이 아닐 경우
          equalDifference = lastNum - int(j)
          lastNum = int(j)
    if count == len(strNum) - 2:
      result += 1
  
print(result)