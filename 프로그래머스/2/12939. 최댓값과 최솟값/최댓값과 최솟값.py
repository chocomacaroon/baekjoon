def solution(s):
    answer = ''
    lst = s.split()
    lst2 = []
    for n in lst:
        lst2.append(int(n))
    answer = str(min(lst2)) + " " + str(max(lst2))
    return answer