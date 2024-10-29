import sys
N = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(N):
    m = int(sys.stdin.readline())
    count[m]+=1

for i,c in enumerate(count):
    if c > 0:
        for _ in range(c):
            print(i)