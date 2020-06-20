import heapq
from collections import deque
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

def networkDelayTime(times, N, K):

    elapsedTime = [0] + [float("inf")] * N
    graph = defaultdict(list)
    heap = [(0, K)]

    # add to adj hash table, where group
    for u, v, w in times:
        graph[u].append((v, w))

    
    while heap:

        # pop off heap/queue
        time, node = heapq.heappop(heap)
        if time < elapsedTime[node]:

            # process (add to elapsed time array)
            elapsedTime[node] = time

            # add neighbours, include weight
            for v, w in graph[node]:
                heapq.heappush(heap, (time + w, v))

    
    mx = max(elapsedTime)
    return mx if mx < float("inf") else -1

print( networkDelayTime(times, N, K) )