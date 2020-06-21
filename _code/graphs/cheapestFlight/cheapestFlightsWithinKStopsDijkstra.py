from collections import deque

'''
https://www.youtube.com/watch?v=Jbb9qNIAyg0
'''
import collections

n = 3
flights = [[0,1,100],[1,2,200],[0,2,500]]
src = 0
dest = 2
k = 1



def findCheapestPrice(n, flights, src, dest, K):

    # d = collections.defaultdict(list)
    # seen = collections.defaultdict(lambda: float('inf'))

    adj = [[] for _ in range(n)]
    output = [float('inf') for _ in range(n)]
    output[src] = 0

    # add to adj list where key is src, and value is destination+cost
    for u, v, w in flights:
        adj[u] += [(v, w)]


    graph = deque()
    graph.append((src, -1))     # where -1 is the number of stops

    while graph:

        u, stop = graph.popleft()
        if stop >= K:
            continue

        for v, w in adj[u]:

            output[v] = output[u]+w
            graph.append((v,stop+1))

    if output[dest] == float('inf'):
        return -1
    else:
        return output[dest]




print( findCheapestPrice(n, flights, src, dest, k) )