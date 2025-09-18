def solution(s):
    answer = 0
    dic = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    tmp = ""
    for c in s:
        if not c.isdigit():
            tmp += c
        else:
            answer = answer*10+int(c)
        if tmp in dic:
            answer = answer*10+dic.index(tmp)
            tmp = ""
    return answer