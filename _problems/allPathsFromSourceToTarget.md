---
layout: page
title:  All Paths from Source To Target
last_solved: 2020-07-24
category: graph, bfs, dfs
leetcode_url: https://leetcode.com/problems/all-paths-from-source-to-target/
status: Attempted
---

Problem
-------

```
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

```

Solution
----------

[Timothy's Change DFS](https://www.youtube.com/watch?v=xM8uxH0vcRw)

{% highlight python %}

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
    end = len(graph)-1
    
    def dfs(node, path, output):
        
        # base condition
        if node == end:
            output.append(path)
                
        for nxt in graph[node]:
            dfs(nxt, path+[nxt], output)
    
    output = []
    dfs( 0, [0], output)
    return output

{% endhighlight %}


My Attempt at DFS
-------------

{% highlight python %}

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
    output = []
    
    def dfs(node, path, outut):    # node is current Node 0,1,2,3
        
        # base condition
        if node==len(graph)-1:
            output.append(path)
        
        else:
            
            # recurse dfs on all children/neighbours
            for neighbour in graph[node]:   
                dfs(neighbour, path + [neighbour], output)
    
    dfs(0, [0], output)
    return output

{% endhighlight %}       
        

![image1]()