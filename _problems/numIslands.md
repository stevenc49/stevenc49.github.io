---
layout: page
title:  Number of Islands
---

Use the flood fill algorithm.

Some gotchas:
- check for string "1" and not integer 1
- check for empty grid "[]"
- can do if (out of bounds) or if curr='1', then many "directional ifs"


{% highlight python %}


def numIslands(self, grid):

    if not grid: return 0
    
    rows = len(grid)
    cols = len(grid[0])

    def dfs(i, j):

        if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]=="0":
            return
        else:
            grid[i][j]="0"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

    count = 0
    for i in range(rows):
        for j in range(cols):

            if grid[i][j]=="1":
                count += 1
                dfs(i, j)

    return count

{% endhighlight %}


The flood fill recursive algorithm could also be written in two ways:

- first with boundary checks
- second with "directional ifs", maybe just forget about this one

The difference is that the first if statements checks for out of bounds and the "0" boundary.

Then you dont have to have "directional ifs" after.

{% highlight python %}

    # Approach 1 - check out of bounds
    def floodFill(grid, r,c):
   
        
        if r < 0 or r >=R or c < 0 or c >= C or grid[r][c] == "0":
            return
        else:
            print(r,c,grid[r][c])

            grid[r][c] = '0'    # mark as visited
            floodFill(grid, r-1, c)
            floodFill(grid, r+1, c)
            floodFill(grid, r, c-1)
            floodFill(grid, r, c+1) 

    # Approach 2
    def floodFill(grid, r,c):

        print(r,c,grid[r][c])

        if grid[r][c] == '1':   # this means we can advance
            grid[r][c] = '0'    # mark as visited
            if r>=1: floodFill(grid, r-1, c)
            if r+1<R: floodFill(grid, r+1, c)
            if c>=1: floodFill(grid, r, c-1)
            if c+1<C: floodFill(grid, r, c+1) 


{% endhighlight %}

![image1]()