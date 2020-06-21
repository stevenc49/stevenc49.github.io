import heapq
from collections import deque
from collections import defaultdict

'''
https://www.youtube.com/watch?v=Jbb9qNIAyg0
'''


n = 3
flights = [[0,1,100],[1,2,200],[0,2,500]]
src = 0
dest = 2
k = 1



def findCheapestPrice(n, flights, src, dest, K):

    output = [float("inf")] * n
    output[src] = 0

    graph = defaultdict(list)
    heap = [(src, -1)]    # dest, costs

    # add to adj hash table
    for u, v, w in flights:
        graph[u].append((v,w))

    while heap:

        v, w = heapq.heappop(heap)

        for v, w in graph[v]:
            output[v] = output[u]+w
            heapq.heappush(heap, (v, output[u]+w))

    print( output )





print( findCheapestPrice(n, flights, src, dest, k) )