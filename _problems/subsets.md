---
layout: page
title:  Subsets
last_solved: 2020-06-22
category: recursion, backtracking
leetcode_url: https://leetcode.com/problems/subsets/
status: Solved
---

Problem
-------

```
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

```

Solution
----------

All backtracking problems have this structure, just memorize it.

Still not sure why we +1 to index and why that is different from Permutation. This series of articles tries to explain it.

[part 1](https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28)
[part 2](https://medium.com/algorithms-and-leetcode/backtracking-with-leetcode-problems-part-2-705c9cc70e52)
[part 3](https://medium.com/algorithms-and-leetcode/in-depth-backtracking-with-leetcode-problems-part-3-b225f19e0d51)


{% highlight python %}

def subsets3(nums):

    def backtrack(currentSubset, allSubsets, nums, index):

        allSubsets.append( currentSubset.copy() )

        for i in range(index, len(nums)):

            currentSubset.append(nums[i])
            print(currentSubset)

            backtrack( currentSubset, allSubsets, nums, i+1 )
            currentSubset.pop()
            print(currentSubset)


    ans = []
    backtrack([], ans, nums, 0)
    return ans

{% endhighlight %}


printing the currentSubset at each iteration looks like this:
```
[1]
[1, 2]
[1, 2, 3]
[1, 2]
[1]
[1, 3]
[1]
[]
[2]
[2, 3]
[2]
[]
[3]
[]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

![image1](https://miro.medium.com/max/1400/1*xrjS6JIZ5f7wFCNBDPrr0g.png)

![image1](https://miro.medium.com/max/1400/1*_s5iiwdZXbg1OFWO9YDjng@2x.jpeg)



______________


Compare these two solutions:

{% highlight python %}

def subsets5(nums):

    def helper(start, currentSubset, allSubsets):

        output.append( currentSubset.copy() )

        for i in range(start, len(nums) ):

            currentSubset.append( nums[i] )
            helper(i+1, currentSubset, output)
            currentSubset.pop()
        
    output = []
    helper(0, [], output)
    return output



'''
    recursion without backtracking from timonthy chang
    https://www.youtube.com/watch?v=Mi_C_CMW7vQ
'''
def subsets4(nums):

    output = []

    def helper(start, currentSubset, output):
        # output += [tmp]
        output.append(currentSubset)
        for i in range(start, len(nums)):
            print( (i+1, currentSubset+[nums[i]]) )
            helper( i+1, currentSubset+[nums[i]], output )
    
    helper(0, [], output)

    return output

{% endhighlight %}

The output is like this:
```
(1, [1])
(2, [1, 2])
(3, [1, 2, 3])
(3, [1, 3])
(2, [2])
(3, [2, 3])
(3, [3])
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

____________


![image1](https://miro.medium.com/max/1050/1*ddhF2JWfmEl8yLwjx5vt7Q.jpeg)
