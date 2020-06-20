---
layout: page
title:  Network Delay Time
last_solved: 2020-06-19
category: graph, dijkstra
leetcode_url: https://leetcode.com/problems/network-delay-time
status: Attempted
---

Problem
-------

```
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.


Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
```

![image1](https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png)

Solution
----------

Dijkstra is written very similar to BFS but with weights.

The end result of this problem is an array that keeps track of elaped time.

```
        node     0,1,2,3,4  <-- index corresponds to node
elapsedTime:    [0,1,0,1,2] <-- value corresponds to time for signal to reach node i from node K (ie: takes 2 seconds to reach node 4 from node 2)

```

{% highlight python %}

import heapq
from collections import deque
from collections import defaultdict

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

def networkDelayTime(times, N, K):

    elapsedTime = [0] + [float("inf")] * N
    graph = defaultdict(list)
    heap = [(0, K)]     # time, start node (ie: (0,2))

    # add to adj hash table, where group
    for u, v, w in times:
        graph[u].append((v, w))

    ###
        graph:
        2: [(1,1),(1,3)]
        3: [(4,1)]
    ###
    
    while heap:

        # pop off heap/queue
        time, node = heapq.heappop(heap)
        if time < elapsedTime[node]:

            # process (add to elapsed time array)
            elapsedTime[node] = time

            # add neighbours, include weight
            for v, w in graph[node]:
                heapq.heappush(heap, (time + w, v))     # at node 3, add neighbour 4 (time+w, v)=(1+1,4) and heap=[(2,4)] -> time to reach node 4=2

    
    mx = max(elapsedTime)
    return mx if mx < float("inf") else -1

print( networkDelayTime(times, N, K) )

{% endhighlight %}


