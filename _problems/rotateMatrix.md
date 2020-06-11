---
layout: page
title:  Rotate Matrix
last_solved: 2020-06-10
category: Matrix
leetcode_url: https://leetcode.com/problems/rotate-image/
status: Solved
---

Problem
-------

```
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

Solution
----------

Transpose and Flip. This is the second time that I'm seeing this and I really worked hard to understand it the first time.

The second time, I was able to:
- recall "the solution"
- code up the solution and get the array indexes and loop ranges correct (things I usually mess up on)

{% highlight python %}

def rotateMatrix(mat):

    N = len(mat)

    # transpose
    for i in range(N):
        for j in range(i, N):

            tmp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = tmp
    
    print( 'after transpose: ',  mat )

    # flip horizontally
    for i in range(N):
        for j in range(N//2):
            
            # swap j and N-j
            tmp = mat[i][j]
            mat[i][j] = mat[i][N-j-1]
            mat[i][N-j-1] = tmp
    
    print( 'after flip: ',  mat )

{% endhighlight %}


![image1]()