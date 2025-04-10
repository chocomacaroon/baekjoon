def solution(n):
    answer = 0
    stand = to_2(n).count('1')
    while True:
        n += 1
        if to_2(n).count('1') == stand:
            return n
    return answer

def to_2(n):
    result = ''
    while n > 0:
        result += str(n%2)
        n//=2
    if n%2==1:
        result += str(n%2)
    return result[::-1]