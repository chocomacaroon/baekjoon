def solution(quiz):
    answer = []
    for s in quiz:
        s = s.split()
        x,op,y,result = s[0],s[1],s[2],s[4]
        if op == "+":
            if int(x) + int(y) == int(result):
                answer.append("O")
            else:
                answer.append("X")
        elif op == "-":
            if int(x) - int(y) == int(result):
                answer.append("O")
            else:
                answer.append("X")
    return answer