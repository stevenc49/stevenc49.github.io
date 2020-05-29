---
layout: page
title:  Set Matrix Zeros
---



From:
{% highlight text %}
  [1,1,1],
  [1,0,1],
  [1,1,1]
{% endhighlight %}
to 
{% highlight text %}
  [1,0,1],
  [0,0,0],
  [1,0,1]
{% endhighlight %}

But instead got this:
{% highlight text %}
  [1,0,0],
  [0,0,0],
  [0,0,0]
{% endhighlight %}


This is because when you do it inplace, it will zero out some cells and the helper function will be called on those ones you already zeroed out.

{% highlight python %}

mat = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]


def setZeroes(mat):

    if not mat: return None

    rows = len(mat)
    cols = len(mat[0])

    def zeroUpward(i,j):

        if i<0: return
        else:
            mat[i][j]=0
            zeroUpward(i-1,j)

    def zeroDownward(i,j):

        if i>=rows: return
        else:
            mat[i][j]=0
            zeroDownward(i+1,j)

    def zeroLeft(i,j):

        if j<0: return
        else:
            mat[i][j]=0
            zeroLeft(i,j-1)

    def zeroRight(i,j):

        if j>=cols: return
        else:
            mat[i][j]=0
            zeroRight(i,j+1)

    for i in range(0, rows):
        for j in range(0, cols):
            if mat[i][j]==0:
                zeroUpward(i,j)
                print("after up", mat)

                zeroDownward(i,j)
                print("after down", mat)

                zeroLeft(i,j)
                print("after left", mat)

                zeroRight(i,j)
                print("after right", mat)

    return mat

setZeroes(mat)

print(mat)


{% endhighlight %}

A solution to this problem is instead of modifying the matrix right away, save the row and columns that need to be zeroed into two sets. Then zero it the rows and columns in the second pass.

The time complexity is O(m*n)

The space complexity is O(m+n)

{% highlight python %}

def setZeroes(self, mat: List[List[int]]) -> None:

    if not mat: return None

    R = len(mat)
    C = len(mat[0])

    zero_rows = set()
    zero_cols = set()

    # iterate over matrix once to add row and column that needs to be zeroed (without modifying it in place yet)
    for i in range(0, R):
        for j in range(0, C):
            if mat[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)

    # go over second time to actually zero out rows and columns
    for i in range(0, R):
        for j in range(0, C):
            if i in zero_rows:
                mat[i][j]=0
            if j in zero_cols:
                mat[i][j]=0

{% endhighlight %}

![image1]()