def solution(s):
    answer = []
    cnt = 0
    zero = 0
    while s != "1":
        zero += s.count('0')
        cnt += 1
        s = s.replace('0', '')
        strlen = len(s)
        new = bin(strlen)[2:]
        s = new
    return [cnt, zero]