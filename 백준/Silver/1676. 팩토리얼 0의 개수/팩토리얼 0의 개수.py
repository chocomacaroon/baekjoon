N = int(input())
sub = 1
for i in range(1, N+1):
    sub *= i
sub = str(sub)
i = len(sub)-1
cnt = 0
while True:
    if sub[i] != '0':
        break
    cnt += 1
    i -= 1
print(cnt)