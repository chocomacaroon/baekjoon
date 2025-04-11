def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = [0]*bridge_length
    waiting = truck_weights
    comp = []
    n = waiting.pop(0)
    # print(n)
    bridge[-1] = n
    while waiting:
        answer+=1
        bridge.pop(0)
        if sum(bridge)+waiting[0] <= weight:
            n = waiting.pop(0)
            bridge.append(n)
        else:
            bridge.append(0)
        # print(bridge)
        # print(waiting)
        # print()
    while bridge:
        answer+=1
        bridge.pop()
    return answer

# 0 7 # 4 5 6
# 7 0 # 4 5 6
# 0 4 # 5 6
# 4 0 # 5 6
# 0 5 # 6
# 5 0 # 6
# 0 6 # []
