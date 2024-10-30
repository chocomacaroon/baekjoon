import sys

input = sys.stdin.readline

N,M = map(int,input().strip().split())
board = []
for _ in range(N):
    s = input().strip()
    board.append(s)

count = []

for i in range(0,N-7):
    for j in range(0,M-7):
        cnt1 = 0
        cnt2 = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                x = board[a][b]
                if (a+b)%2==0 and x=="B":
                    cnt1+=1
                elif (a+b)%2==0 and x == "W":
                    cnt2+=1
                elif (a+b)%2==1 and x == "B":
                    cnt2+=1
                elif (a+b)%2==1 and x == "W":
                    cnt1+=1
        count.append(min(cnt1,cnt2))
print(min(count))


