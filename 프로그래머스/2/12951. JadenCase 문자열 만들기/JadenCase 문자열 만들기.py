def solution(s):
    answer = ''
    flag = True
    for c in s:
        if c == ' ':
                flag = True
                answer += c
        elif flag:  
            if c.isalpha():
                answer += c.upper()
            else:
                answer += c
            flag = False
        else:
            if c == ' ':
                flag = True
                answer += c
            elif c.isalpha():
                answer += c.lower()
            else:
                answer += c
        
    return answer