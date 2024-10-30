import sys

input = sys.stdin.readline

K = int(input().strip())
nums = []
for _ in range(K):
    c = int(input().strip())
    if c == 0:
        nums.pop()
    else:
        nums.append(c)
print(sum(nums))