def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        return 5*len(cities)
    for n in cities:
        if n.lower() not in cache:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(n.lower())
            answer += 5
        else:
            cache.remove(n.lower())
            cache.append(n.lower())
            answer += 1
    return answer