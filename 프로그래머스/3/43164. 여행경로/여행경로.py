ways = []

def dfs(start, tickets, rout, used):
    global ways
    
    for i, (s, e) in enumerate(tickets):
        if s == start and not used[i]:
            used[i] = True
            dfs(e, tickets, rout+[e], used)
            used[i] = False
    if all(used):
        ways.append(rout)


def solution(tickets):
    answer = []
    
    used = [False] * len(tickets)
    
    dfs("ICN", tickets, [], used)
    ways.sort()
    return ["ICN"] + ways[0]
    return answer