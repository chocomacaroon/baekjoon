def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        tmp = b[:]
        for c in can:            
            tmp = tmp.replace(c,"@"*len(c))
        if tmp == "@"*len(b):
            answer += 1
    return answer

#maya