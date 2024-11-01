import sys
input = sys.stdin.readline

W,H,X,Y,P = map(int,input().strip().split())
cnt = 0
for _ in range(P):
    x,y = map(int,input().strip().split())
    if (X <= x <= X+W and Y <= y <= Y+H):
        cnt += 1
    elif (x <= X and (X-x)**2+(Y+H/2-y)**2 <= (H/2)**2):
        cnt += 1
    elif (x >= X+W and (X+W-x)**2+(Y+H/2-y)**2 <= (H/2)**2):
        cnt += 1
print(cnt)