---
layout: page
title:  Validate Sudoku
last_solved: 2020-06-10
category: matrix
leetcode_url: https://leetcode.com/problems/valid-sudoku/
status: Solved
---

Problem
-------

```
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

```

Solution
----------

{% highlight python %}

def validateBoard(bo):

    rows = [ set() for i in range(9) ]
    cols = [ set() for i in range(9) ]
    boxes = [ set() for i in range(9) ]

    for i in range(9):
        for j in range(9):

            val = bo[i][j]
            if val==".":
                continue


            # validate row
            if val in rows[i]:

                print( val + "already in row %s" % i )
                return False
            else:
                rows[i].add( val )

            # validate col
            if val in cols[j]:

                print( val + "already in col %s" % j )
                return False
            else:
                cols[j].add( val )

            # validate box
            k = (i//3)*3 + (j//3)
            if val in boxes[k]:

                print( val + "already in box %s" % k )
                return False
            else:
                boxes[k].add( val )

    return True

{% endhighlight %}


![image1]()