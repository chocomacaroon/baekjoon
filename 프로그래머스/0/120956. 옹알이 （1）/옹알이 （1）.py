def solution(babbling):
    answer = 0
    joka = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        for j in joka:
            if j in b:
                b = b.replace(j," ")
        if len(b.split()) == 0:
            answer += 1
    return answer