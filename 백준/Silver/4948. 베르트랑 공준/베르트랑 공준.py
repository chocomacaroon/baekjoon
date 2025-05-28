def arato(s,e):
    is_Prime = [True] * (e+1)
    for i in range(2, int(e**(0.5))+1):
        if is_Prime[i]:
            for j in range(i*i, e+1, i):
                is_Prime[j] = False
    return len([i for i in range(s,e+1) if is_Prime[i]])

while True:
    n = int(input())
    if n == 0: break
    res = arato(n+1, 2*n)
    print(res)