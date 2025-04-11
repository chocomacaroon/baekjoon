def solution(array):
    answer = 0
    lst = []
    for n in array:
        if [n,array.count(n)] not in lst:
            lst.append([n,array.count(n)])
    lst.sort(key = lambda x:-x[1])
    if len(lst)==1:
        return lst[0][0]
    elif lst[0][1] == lst[1][1]:
        return -1
    else:
        return lst[0][0]
    return answer