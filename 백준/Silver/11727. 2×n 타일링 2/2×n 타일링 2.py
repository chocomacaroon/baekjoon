n = int(input())

def combi(n,r):
    up = 1
    for i in range(n-r+1, n+1):
        up *= i
    for i in range(1,r+1):
        up //= i
    return up
res = 0

for i in range(n+1):
    if n-i < i:
        break
    res += combi(n-i,i)*(2**i)
print(res%10007)