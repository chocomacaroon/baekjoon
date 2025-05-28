
n = int(input())

answer = 0

def combi(n,r):
    up = 1
    for i in range(n-r+1, n+1):
        up *= i
    down = 1
    for i in range(1,r+1):
        down *= i
    # print(f"combi {n} {r} {up//down}")
    return up//down

for i in range(n):
    if n - i < i: break
    answer += combi(n-i,i)

print(answer%10007)