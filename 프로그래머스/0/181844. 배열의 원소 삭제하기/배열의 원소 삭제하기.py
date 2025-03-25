def solution(arr, delete_list):
    answer = []
    for a in arr:
        if a in delete_list:
            pass
        else:
            answer.append(a)
    return answer