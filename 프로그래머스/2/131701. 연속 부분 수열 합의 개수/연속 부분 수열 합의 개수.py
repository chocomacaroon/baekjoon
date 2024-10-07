def solution(elements):
    answer = 0
    su=0
    s = set()
    lenght = len(elements)
    for n in range(1,lenght+1):
        elements.append(elements[n-1])
        for i in range(len(elements)-n):
            su = sum(elements[i:i+n])
            s.add(su)
    return len(s)
    return answer