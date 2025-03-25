def solution(binomial):
    answer = 0
    x,op,y = binomial.split()
    if op == "+":
        return int(x) + int(y)
    elif op == "-":
        return int(x) - int(y)
    elif op == "*":
        return int(x) * int(y)
    return answer