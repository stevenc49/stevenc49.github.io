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


Initialially tried this but the result wasn't what I expected. I got this:

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


![image1]()