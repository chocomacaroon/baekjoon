def solution(arr1, arr2):
    answer = []
    for v1,v2 in zip(arr1,arr2):
        tmp = []
        for i,j in zip(v1,v2):
            tmp.append(i+j)
        answer.append(tmp)
    return answer