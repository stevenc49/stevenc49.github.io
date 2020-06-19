---
layout: page
title:  Island Perimeter
last_solved: 2020-06-19
category: matrix
leetcode_url: https://leetcode.com/problems/island-perimeter
status: Solved
---

Problem
-------

Iterate thru matrix. If cell==1, add 4.
If it has a left or top border, subtract 2.

```

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

```

![image1](https://assets.leetcode.com/uploads/2018/10/12/island.png)

Solution
----------

{% highlight python %}

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        perimeter = 0
        
        for x,y in product(range(R), range(C)):
            
            if grid[x][y]==1:
                
                perimeter+=4
            
                if x>0 and grid[x-1][y]==1:
                    perimeter-=2

                if y>0 and grid[x][y-1]==1:
                    perimeter-=2
    
        
        return perimeter

{% endhighlight %}


