import heapq
from collections import deque
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

def networkDelayTime(times, N, K):

    elapsedTime, graph, heap = [0] + [float("inf")] * N, defaultdict(list), [(0, K)]
    for u, v, w in times:
        graph[u].append((v, w))
    while heap:
        time, node = heapq.heappop(heap)
        if time < elapsedTime[node]:
            elapsedTime[node] = time
            for v, w in graph[node]:
                heapq.heappush(heap, (time + w, v))
    mx = max(elapsedTime)
    return mx if mx < float("inf") else -1

print( networkDelay(times, N, K) )