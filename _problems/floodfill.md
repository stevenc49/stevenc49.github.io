---
layout: page
title:  Flood Fill
---

Be careful with this critical tranversal section, if you make a mistake (ie: > instead of <, than it may not visit the entire grid)

{% highlight text %}

if r>=1: dfs(r-1, c)    # go up
if r+1<R: dfs(r+1, c)   # go down
if c>=1: dfs(r, c-1)    # go left
if c+1<C: dfs(r, c+1)   # go right

{% endhighlight %}


{% highlight python %}

image = [[1,1,1],
        [1,1,0],
        [1,0,1]]


def floodFill(image, startRow, startCol, newColor):

    R = len(image)
    C = len(image[0])
    oldColor = image[startRow][startCol]
    if oldColor == newColor: return image

    def dfs(r, c):

        print(r,c)

        if image[r][c] == oldColor:     # choose whether or not to advance
            image[r][c] = newColor      # process the current node
            if r>=1: dfs(r-1, c)    # go up
            if r+1<R: dfs(r+1, c)   # go down
            if c>=1: dfs(r, c-1)    # go left
            if c+1<C: dfs(r, c+1)   # go right

    dfs(startRow, startCol) # mutates image, but doesn't return image
    return image

print(floodFill(image, 1,1,2))  

[[2, 2, 2],
 [2, 2, 0],
 [2, 0, 1]]

{% endhighlight %}


![image1]()