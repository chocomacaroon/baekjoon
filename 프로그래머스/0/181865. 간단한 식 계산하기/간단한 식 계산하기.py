def solution(binomial):
    answer = 0
    n1,op,n2 = binomial.split()
    if op == '+':
        return int(n1) + int(n2)
    elif op == '-':
        return int(n1) - int(n2)
    elif op == '*':
        return int(n1) * int(n2)
    return answer