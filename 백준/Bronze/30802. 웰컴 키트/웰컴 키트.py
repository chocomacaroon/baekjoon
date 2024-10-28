import math

n = int(input())
sum = 0
sum2 = 0
clothes = list(map(int, input().split()))
t,p = map(int, input().split())
for n in clothes:
    sum += math.ceil(n/t)
    sum2 += n
print(sum)
print(sum2//p, sum2%p)
