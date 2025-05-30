N = int(input())
dp = [0]*(N+1)
# dp[i] : 숫자 i를 1로 만들기 위한 최소 연산 횟수
dp[1] = 0
#3
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i%3==0:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[N])