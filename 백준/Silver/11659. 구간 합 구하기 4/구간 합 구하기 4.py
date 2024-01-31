import sys
M, N = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum = [0]
for i in range(M):
    sum.append(sum[i]+arr[i])
for i in range(N):
    i, j = map(int, sys.stdin.readline().split())
    print(sum[j]-sum[i-1])