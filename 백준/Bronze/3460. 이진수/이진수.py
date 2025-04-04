T = int(input())

for i in range(T):
    n = int(input())
    num = []
    while n//2 > 0:
        num.append(n%2)
        # print(n//2)
        n //= 2
    num.append(n%2)
    num.append(n//2)
    # print(num)
    for k in range(len(num)):
        if num[k] == 1:
            print(k, end = ' ')