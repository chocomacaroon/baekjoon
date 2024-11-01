import sys
input = sys.stdin.readline

N = int(input().strip())

answer = 0

while True:
    if N < 2:
        break
    elif N%5:
        N -= 2
        answer+=1
    else:
        N -= 5
        answer +=1

if N%2:
    print(-1)
else:
    print(answer)