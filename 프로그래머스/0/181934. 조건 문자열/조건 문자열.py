def solution(ineq, eq, n, m):
    answer = 0
    if ineq == "<" and eq == "=":
        return int(n<=m)
    if ineq == "<" and eq == "!":
        return int(n<m)
    if ineq == ">" and eq == "=":
        return int(n>=m)
    if ineq == ">" and eq =="!":
        return int(n>m)
    return answer