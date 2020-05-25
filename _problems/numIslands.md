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


grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","1","0"]
]



def numIslands(grid):

    R = len(grid)
    C = len(grid[0])
    numIslands = 0

    def floodFill(grid, r,c):

        # Approach 1
        print(r,c,grid[r][c])

        if grid[r][c] == '1':   # this means we can advance
            grid[r][c] = '0'    # mark as visited
            if r>=1: floodFill(grid, r-1, c)
            if r+1<R: floodFill(grid, r+1, c)
            if c>=1: floodFill(grid, r, c-1)
            if c+1<C: floodFill(grid, r, c+1) 

    
    for i in range(R):
        for j in range(C):
            if grid[i][j]=='1':
                numIslands+=1
                floodFill(grid, i, j)
    

    print(grid)
    return numIslands

print(numIslands(grid))

{% endhighlight %}


The flood fill recursive algorithm could also be written as the following.

The difference is that the first if statements checks for out of bounds and the "0" boundary.

Then you dont have to have "directional ifs" after.

{% highlight python %}

    def floodFill(grid, r,c):
   
        # Approach 2 - check out of bounds
        if r < 0 or r >=R or c < 0 or c >= C or grid[r][c] == "0":
            return
        else:
            print(r,c,grid[r][c])

            grid[r][c] = '0'    # mark as visited
            floodFill(grid, r-1, c)
            floodFill(grid, r+1, c)
            floodFill(grid, r, c-1)
            floodFill(grid, r, c+1) 

{% endhighlight %}

![image1]()