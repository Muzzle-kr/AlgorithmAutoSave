H, M, S = map(int, input().split())
D = int(input())

H += D // 3600
M += D % 3600 // 60
S += D % 3600 % 60

if S >= 60:
  tmp = S // 60
  S = S % 60
  M += tmp
  
if M >= 60:
  tmp = M // 60
  M = M % 60
  H += tmp

H = H % 24

print(H, M, S, sep=" ")