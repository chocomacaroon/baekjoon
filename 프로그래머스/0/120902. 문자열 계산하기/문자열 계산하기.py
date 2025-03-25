def solution(my_string):
    answer = 0
    st = my_string.split()
    op = "+"
    for i,s in enumerate(st):
        if s == "+":
            op = "+"
        elif s == "-":
            op = "-"
        else:
            if op == "+":
                answer += int(s)
            elif op == "-":
                answer -= int(s)
    return answer