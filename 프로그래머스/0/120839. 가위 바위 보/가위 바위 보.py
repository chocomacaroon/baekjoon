def solution(rsp):
    answer = ''
    for n in rsp:
        if n == '0' : 
            answer += '5'
        elif n == '2' : 
            answer += '0'
        elif n == '5' : 
            answer += '2'
    return answer