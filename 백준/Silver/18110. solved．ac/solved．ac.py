import sys

input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
else:
    nums = []
    for _ in range(N):
        nums.append(int(input()))
    nums.sort()
    x = round(N*0.15+0.0000001)
    nums2 = nums[x:N-x]
    print(round(sum(nums2)/len(nums2)+0.0000001))