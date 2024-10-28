n = int(input())
num = 1
i=6
cnt = 1
while True:
    if num >= n:
        print(cnt)
        break
    num += 6 * cnt
    cnt += 1