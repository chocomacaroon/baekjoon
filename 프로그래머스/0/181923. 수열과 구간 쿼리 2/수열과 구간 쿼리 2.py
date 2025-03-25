def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        sort = sorted(arr[s:e+1])
        # answer.append(sort)
        for i in sort:
            if i > k:
                answer.append(i)
                break
        if sort[-1] <= k:
            answer.append(-1)
    return answer