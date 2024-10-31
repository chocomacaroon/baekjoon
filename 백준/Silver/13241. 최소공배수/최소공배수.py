import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())

def gcd(a,b):
    while b>0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

print(lcm(N,M))
