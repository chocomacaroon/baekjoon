import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    gcd = math.gcd(numer1*denom2 + numer2*denom1, denom1*denom2)
    answer = [(numer1*denom2 + numer2*denom1)//gcd, (denom1*denom2)//gcd]
    return answer

