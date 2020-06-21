---
layout: page
title:  Cheapest Flight Within K Stops
last_solved: 2020-06-20
category: graph, dijkstra
leetcode_url: https://leetcode.com/problems/cheapest-flights-within-k-stops
status: Attempted
---

Problem
-------

```
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

```

![image1](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png)

Solution
----------

Variation on Dijkstra (see network delay problem)

The end result of this problem is an array that keeps track of costs.

Value is the cost it takes to get to get from ```src``` node to ```dest``` node.

```
output:  [0, 100, 300]

```

{% highlight python %}

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

{% endhighlight %}


___________-

Tried Dijkstra on my own but no luck.

{% highlight python %}

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

{% endhighlight %}