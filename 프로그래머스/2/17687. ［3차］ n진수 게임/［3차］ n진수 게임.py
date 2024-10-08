def solution(n, t, m, p):
    result = ''
    x = 0
    cnt = 0
    while True:
        result += convert(x,n)
        x+=1
        if len(result) > t*m:
            result = result[:t*m]
            return result[p-1::m]

def convert(x,n):
    tmp = ""
    num = list("0123456789ABCDEF")
    while True:
        tmp+=num[x%n]
        x = x//n
        if x//n==0:
            if x%n!=0:
                return (tmp+num[x%n])[::-1]
            else:
                return tmp[::-1]
        