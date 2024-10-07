#numpy append
import numpy as np

def solution(arr1, arr2):
    answer = []
    n1 = len(arr2)
    m1 = len(arr2[0])
    new_arr2 = []
    for j in range(m1):
        tmp1 = [arr2[i][j] for i in range(n1)]
        new_arr2.append(tmp1)
    arr1 = np.array(arr1)
    new_arr2 = np.array(new_arr2)
    tmp = []
    for n in arr1:
        tmp = [int(np.dot(n,m)) for m in new_arr2]
        answer.append(tmp)        
    return answer
    