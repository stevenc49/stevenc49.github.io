---
layout: page
title:  Prison cells after n days
last_solved: 2020-07-01
category: arrays
leetcode_url: https://leetcode.com/problems/prison-cells-after-n-days/
status: Semi-Solved
---

Problem
-------

```
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

```

Solution
----------

{% highlight python %}

arr = [0,1,0,1,1,0,0,1]
N=7


def prisonAfterNDays(arr, N):

    arr2 = [0]*len(arr)

    for i in range(N):

        for i in range(1, len(arr)-1):
            
            # not xor the middle
            arr2[i] = int(not arr[i-1] ^ arr[i+1])

            # make ends zero
            arr2[0], arr2[len(arr)-1] = 0,0

        # copy arr2 to arr
        arr = arr2.copy()
    
    return arr

print(prisonAfterNDays(arr, N))


{% endhighlight %}


![image1]()