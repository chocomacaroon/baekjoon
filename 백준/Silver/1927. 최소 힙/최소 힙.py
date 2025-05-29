import heapq
import sys

heap = []

N = int(sys.stdin.readline())

for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heapq.heappush(heap, n)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)