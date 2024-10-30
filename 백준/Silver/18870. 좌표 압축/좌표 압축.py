import sys

input = sys.stdin.readline

N = int(input())
l = list(map(int, input().strip().split()))
rank = sorted(set(l))
rank_dict = {}

for i in range(len(rank)):
    rank_dict[rank[i]] = i

for n in l:
    print(rank_dict[n],end=' ')