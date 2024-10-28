chess = []
cnt = 0
for i in range(8):
    chess = list(input())
    for j in range(len(chess)):
        if (i+j)%2==0 and chess[j] == "F":
            cnt += 1
print(cnt)

