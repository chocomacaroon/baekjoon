N,A,B = map(int,input().split())
good = 1
bad = 1
for _ in range(N):
    good += A
    bad += B
    if bad > good:
        bad,good = good,bad
    elif bad == good:
        bad -= 1
print(good, bad)