import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙으로 변환 (O(N))
    answer = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b * 2)
        answer += 1

    return answer
