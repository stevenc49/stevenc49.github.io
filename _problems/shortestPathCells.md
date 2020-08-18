---
layout: page
title:  Shortest Cell Path
last_solved: 
category: 
leetcode_url: https://www.pramp.com/challenge/Y56aZmaj9Ptmd9wV9xvL
status: Attempted
---

Problem
-------

```
Shortest Cell Path
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011

```

Solution
----------



Have to use BFS because BFS finds the shortest path. DFS doesn't

None of the solutions below returns the correct result.

{% highlight python %}

    q = [(sr,sc, 0)]
    seen = set()
  
    while q:

      r,c,depth = q.pop(0)

      if r==tr and c==tc: return depth

      # loop thru all dirs
      for (nr, nc) in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):

        # check if within bounds and not visited:
        if 0<=nr<len(grid) and 0<=nc<len(grid) and grid[nr][nc]==1 and (nr,nc) not in seen:

          q.append((nr, nc, depth+1))
          seen.add((nr,nc))

    return -1

_______________



    queue = [(sr, sc, 0)]
    seen = set()
    seen.add((sr, sc))

    while queue:
        r, c, depth = queue.pop(0)
        if r == tr and c == tc: return depth
        for (nr, nc) in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 1 and (nr, nc) not in seen:
                queue.append((nr, nc, depth + 1))
                seen.add((nr, nc))

    return -1



________________


        ans, m, n = 0, len(grid), len(grid[0])
        #if grid[0][0] == 1 or grid[m-1][n-1] == 1: return -1
        q = [(sr, sc)]
        while q:
            tmp_q = []
            ans += 1
            while q:
                x, y = q.pop()
                
                print(x,y)
                
                if (x, y) == (tr, tc): return ans
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    xx, yy = x+dx, y+dy
                    if 0 <= xx < m and 0 <= yy < n and not grid[xx][yy]:
                        grid[xx][yy] = 1
                        tmp_q.append((xx, yy))
            q = tmp_q
        return -1

{% endhighlight %}


![image1]()