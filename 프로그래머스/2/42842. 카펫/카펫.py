def solution(brown, yellow):
    answer = []
    
    for w in range(3, int(brown/2)+1):
        h = (brown - w*2)/2 + 2
        if (w-2)*(h-2) == yellow:
            return [h, w]
    return answer