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

My solution that worked for small test cases but reached TLE when N=1000000000

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

__________________

Even adding a memo didn't help. N=1 000 000 000 took a while and didnt complete.

{% highlight python %}

arr = [0,1,0,1,1,0,0,1]
N=6

def prisonAfterNDays(arr, N):

    def computeNext(arr):

        arr2 = [0]*len(arr)
        
        for i in range(1, len(arr)-1):
            
            # not xor the middle
            arr2[i] = int(not arr[i-1] ^ arr[i+1])

            # make ends zero
            arr2[0], arr2[len(arr)-1] = 0,0

        # copy arr2 to arr
        return arr2.copy()


    memo = {}

    for i in range(N):

        if tuple(arr) not in memo:
            old_arr = arr
            new_arr = computeNext(arr)

            memo[tuple(old_arr)] = new_arr
            arr = new_arr
        else:
            arr = memo[tuple(arr)]

    print(memo)
    return arr

print( prisonAfterNDays(arr, N) )

{% endhighlight %}

_____________________


After failing to get the hashmap solution to run in time. I checked out [how other ppl did it](https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14)] and their solution ran in time. Will revisit this.

{% highlight python %}

arr = [0,1,0,1,1,0,0,1]
N=1000000000
# N=7

def prisonAfterNDays(arr, N):

    def computeNext(arr):

        arr2 = [0]*len(arr)
        
        for i in range(1, len(arr)-1):
            
            # not xor the middle
            arr2[i] = int(not arr[i-1] ^ arr[i+1])

            # make ends zero
            arr2[0], arr2[len(arr)-1] = 0,0

        # copy arr2 to arr
        return arr2.copy()



    seen = {str(arr): N}
    while N:
        seen.setdefault(str(arr), N)
        N -= 1
        # arr = [0] + [arr[i - 1] ^ arr[i + 1] ^ 1 for i in range(1, 7)] + [0]
        arr = computeNext(arr)
        if str(arr) in seen:
            N %= seen[str(arr)] - N
        
    return arr


print( prisonAfterNDays(arr, N) )

{% endhighlight %}

![image1]()