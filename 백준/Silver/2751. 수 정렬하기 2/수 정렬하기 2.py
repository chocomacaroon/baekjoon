import sys
N = int(input())
S = list(map(int, sys.stdin.readlines()))
S.sort()
print(*S, sep = '\n')