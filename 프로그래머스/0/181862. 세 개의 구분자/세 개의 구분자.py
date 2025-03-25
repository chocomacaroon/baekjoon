def solution(myStr):
    answer = []
    myStr = myStr.replace('a',' ')
    myStr = myStr.replace('b',' ')
    myStr = myStr.replace('c',' ')
    answer = myStr.split()
    return answer if len(answer) else ["EMPTY"]