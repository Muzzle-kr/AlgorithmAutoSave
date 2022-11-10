result = 0
for i in range(1, int(input()) + 1):
  if len(str(i)) < 3:
    result += 1
  else:
    # print(f"요기요!! {i}번째")
    strNum = str(i)
    equalDifference = -1001
    lastNum = 0
    count = 0
    # 자릿수 반복
    for idx, j in enumerate(strNum):
      # print(f'idx: {idx}, j = {j}')
      # idx가 0일 경우
      if idx == 0:
        # lastNum을 strNum[0]으로 치환
        lastNum = int(j)
      # idx가 1 이상일 경우
      else:
        if equalDifference != -1001:
            if equalDifference == lastNum - int(j):
              # print(f'equalDifference: {equalDifference}, lastNum: {lastNum}, int(j): {int(j)}')
              # 등차수열일 경우 count
              count += 1
              lastNum = int(j)
            else:
              # print(f'equalDifference: {equalDifference}, lastNum: {lastNum}, int(j): {int(j)}')
              # 등차수열이 아닐 경우
              equalDifference = lastNum - int(j)
              lastNum = int(j)
        else:
          # print(f'equalDifference: {equalDifference}, lastNum: {lastNum}, int(j): {int(j)}')
          # 등차수열이 아닐 경우
          equalDifference = lastNum - int(j)
          lastNum = int(j)
    # print(f'현재 count: {count}, len(strNum) - 1: {len(strNum)-1}')
    if count == len(strNum) - 2:
      result += 1
  
print(result)