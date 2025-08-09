def solution(arr1, arr2):
    answer = []
    for x1 in range(len(arr1)):
        tmp = []
        for y1 in range(len(arr2[0])):
            su = 0
            for y2 in range(len(arr1[0])):
                su += arr1[x1][y2] *arr2[y2][y1]
            tmp.append(su)
        answer.append(tmp)
    return answer