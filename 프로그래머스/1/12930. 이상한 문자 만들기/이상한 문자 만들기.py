def solution(s):
    answer = ''
    i = 0
    for c in s:
        if c == ' ':
            i = 1
        i += 1
        if i%2:
            answer += c.upper()
        else:
            answer += c.lower()
    return answer