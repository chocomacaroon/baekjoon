import sys
input = sys.stdin.readline
N = int(input().strip())
nums = []
for _ in range(N):
    nums.append(int(input().strip()))
for n in sorted(nums, reverse=True):
    print(n)
