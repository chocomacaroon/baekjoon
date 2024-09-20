

def solution(my_string):
    answer = ''
    for c in my_string:
        if(c.islower()):
            answer += c.upper()
        if(c.isupper()):
            answer += c.lower()
    return answer