N, M = map(int, input().split())
arr = list(map(int, input().split()))
lt = 0
rt = 1
if N == 1:
  if arr[0] == M:
    print(1)
  else:
    print(0)
else:
  total = arr[lt] + arr[rt]
  count = 0
  # M보다 값이 크다면 lt를 한 칸 추가한다.
  # M보다 값이 작다면 rt를 한 칸 추가한다.
  # M과 값이 같다면 lt,rt를 한 칸씩 추가한다.
  if arr[lt] == M:
    count += 1

  while rt < N or lt < rt:
    # print(f"lt = {lt}, rt = {rt}, total = {total}")
    try:
      if total == M:
        count += 1
        total -= arr[lt]
        lt += 1
        rt += 1
        total += arr[rt]
      elif total < M:
        rt += 1
        total += arr[rt]
      else:
        total -= arr[lt]
        lt += 1
    except:
      # print(f"탈출 조건 lt = {lt}, rt = {rt}")
      break
  print(count)