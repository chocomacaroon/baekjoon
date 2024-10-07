import math

# def solution(n):
#     ans = 0
#     x = 2
#     while n > 0:
#         n -= pow2(n)
#         ans+=1
#     return ans

# def pow2(n):
#     # return 2**int(math.log(n,2))
#     x = 1
#     while x*2<=n:
#         x *= 2
#     return x


def solution(n):
    ans = 0
    while True:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n //= 2
        if n == 0:
            return ans
    return ans
