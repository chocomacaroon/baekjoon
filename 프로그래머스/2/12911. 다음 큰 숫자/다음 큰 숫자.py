def solution(n):
    answer = 0
    target = bin(n)[2:].count('1')
    while True:
        n += 1
        new = bin(n)[2:]
        if new.count('1') == target:
            return n
    return answer