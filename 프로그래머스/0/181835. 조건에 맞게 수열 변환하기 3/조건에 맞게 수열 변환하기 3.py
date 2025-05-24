def solution(arr, k):
    if k%2:
        return [n*k for n in arr]
    else:
        return [n+k for n in arr]