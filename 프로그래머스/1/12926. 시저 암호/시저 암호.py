def solution(s, n):
    answer = ''
    for c in s:
        if c.isalpha():
            for i in range(n):
                if c == 'z':
                    c = 'a'
                elif c == 'Z':
                    c = 'A'
                else:
                    c = chr(ord(c)+1)
        answer += c
    return answer