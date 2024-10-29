import sys
input = sys.stdin.readline
N = int(input().strip())
card1 = list(map(int, input().strip().split()))
card1_cnt = {}

for c in card1:
    if c in card1_cnt.keys():
        card1_cnt[c] += 1
    else:
        card1_cnt[c] = 1

M = int(input())

card2 = list(map(int, input().strip().split()))
for c in card2:
    if c in card1_cnt:
        print(card1_cnt[c], end=" ")
    else:
        print(0,end=" ")