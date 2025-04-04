N = int(input())
cups = [i for i in range(1,5)]
for i in range(N):
    a, b = map(int, input().split())
    #컵을 바꾼다. 그 컵이 있는 위치
    idxa = cups.index(a)
    idxb = cups.index(b)
    cups[idxa], cups[idxb] = cups[idxb], cups[idxa]
print(cups[0])