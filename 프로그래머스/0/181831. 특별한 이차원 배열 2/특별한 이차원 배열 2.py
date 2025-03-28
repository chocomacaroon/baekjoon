def solution(arr):
    answer = 1
    for i in range(len(arr[0])):
        for j in range(i+1,len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return answer