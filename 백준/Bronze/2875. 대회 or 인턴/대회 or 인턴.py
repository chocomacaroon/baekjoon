N, M, K = map(int, input().split())
T = min(N//2, M)
girl_rest = N - T*2
boy_rest = M - T
if boy_rest+girl_rest < K:
  K = K - boy_rest - girl_rest
  rest = K//3
  if K%3 > 0:
    rest += 1
  if rest>T:
    T = 0
  else:
    T -= rest
print(T)