import sys
input = sys.stdin.readline
n = int(input().strip())
time = list(map(int, input().strip().split()))
time.sort()
total = 0
answer = 0
for t in time:
    total += t
    answer += total
print(answer)