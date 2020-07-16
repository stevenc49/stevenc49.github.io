---
layout: page
title:  Spiral Matrix
last_solved: 2020-07-16
category: matrix
leetcode_url: https://leetcode.com/problems/spiral-matrix/
status: Attempted
---

Problem
-------

```
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

```

Solution
----------

This is a really good problem to practice reverse for loops and matrix traversal

{% highlight python %}


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

def spiralMatrix(matrix):

    start_row = 0
    end_row = len(matrix)
    start_col = 0
    end_col = len(matrix)

    output = []
    while start_row<end_row or start_col<end_col:
        # right
        for i in range(start_col, end_col):
            output.append( matrix[start_row][i] )

        start_row+=1

        # down
        for i in range(start_row, end_row):
            output.append( matrix[i][end_col-1] )

        end_col-=1

        # left
        for i in range(end_col-1, start_col-1, -1):
            output.append( matrix[end_row-1][i] )

        end_row-=1

        # up
        for i in range(end_row-1, start_row-1, -1):
            output.append( matrix[i][start_col] )

        start_col+=1

    return output

print( spiralMatrix(matrix) )

{% endhighlight %}

__________


Dealing with the "edge cases" proved a bit difficult. Would need to analyze this a bit further:

{% highlight python %}

matrix1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

matrix2 = [
  [1, 2, 3, 4],
  [4,5,6,7],
  [7,8,9,10]
]

matrix3 = [
    [2,5,8],[4,0,-1]
]

def spiralMatrix1(matrix):

    if not matrix: return []

    start_row = 0
    end_row = len(matrix)
    start_col = 0
    end_col = len(matrix[0])

    output = []
    while start_row<end_row and start_col<end_col:      # also note the 'or' changed to an 'and'
        # right
        for i in range(start_col, end_col):
            output.append( matrix[start_row][i] )

        start_row+=1

        # down
        for i in range(start_row, end_row):
            output.append( matrix[i][end_col-1] )


        end_col-=1

        if end_row <= start_row: break  # handles edge case with matrix2

        # left
        for i in range(end_col-1, start_col-1, -1):
            output.append( matrix[end_row-1][i] )

        end_row-=1

        if end_col <= start_col: break  # handles edge case with matrix2

        # up
        for i in range(end_row-1, start_row-1, -1):
            output.append( matrix[i][start_col] )

        start_col+=1

    return output




print( spiralMatrix1(matrix3) )

{% endhighlight %}

![image1]()