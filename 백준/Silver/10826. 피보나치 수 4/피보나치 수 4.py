import sys
input = sys.stdin.readline

N = int(input().strip())

n1 = 1
n2 = 1
if N == 0:
    print(0)
elif N == 1 or N == 2:
    print(1)
else:
    for _ in range(N-2):
        n1,n2 = n2,n1+n2
    print(n2)