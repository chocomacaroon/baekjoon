def solution(q, r, code):
    answer = ''
    answer = "".join([code[i] for i in range(r, len(code), q)])
    return answer