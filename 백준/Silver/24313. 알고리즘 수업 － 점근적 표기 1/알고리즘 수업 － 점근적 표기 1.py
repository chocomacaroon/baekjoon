import sys
input = sys.stdin.readline

a,b = map(int,input().strip().split())
c = int(input().strip())
n0 = int(input().strip())

if a*n0+b<=c*n0 and a<=c:
    print(1)
else:
    print(0)

# M/(c-N) <= n0 <= n
# f(n)<=c*n
#an+b<=c*n   n>n0모든 n이 만족해야됨
# b