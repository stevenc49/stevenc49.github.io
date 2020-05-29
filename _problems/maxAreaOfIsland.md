---
layout: page
title:  Max Area of Island
---

Similiar to numIsland, use flood fill and use ```nonlocal``` count variable to keep scope within nested function.

```nonlocal``` means it is not binded to the inner function. And it must be referenced in the outer function (binded to by the outer function)

{% highlight python %}

def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
    if not grid: return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    
    def dfs(i, j):
    
        nonlocal count
    
        if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:
            return count
        else:
            grid[i][j]=0 # mark as visited
            count+=1     # increment nonlocal count
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
            return count
        
    
    count = 0
    maxArea = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                
                count = 0   # set nonlocal count to 0
                
                dfs(i,j)
                
                if count > maxArea:
                    maxArea = count
    
                count = 0   # reset nonlocal count
                
    
    return maxArea

{% endhighlight %}


![image1]()