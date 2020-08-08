---
layout: page
title:  Subsets (Backtracking)
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

______________


![image1](https://5wlqpa.dm.files.1drv.com/y4mWw6FM6vfQ2uGgQLZVTXK03b2a4oZzG94ARUypRFP8T48s5todh08mGzzH5CVx79cVUGI-lKe00r0vgEJt0PlTTYmYze-M_EXdkfEaUTggaMMsCwXXKXHUC3ko0ITL_jl14nHjNEXlI5I3kh3AnD98MerAvWU3GuICbnIDQETihjZo-F86GzUuLYTn-2Q-ZoddrY1zu3b6rchFalBW9mJEQ?width=2425&height=1523&cropmode=none)
![image1](https://5wjpha.dm.files.1drv.com/y4mECUr_-JYl8Sn_JLbFcKa5QKYMklb32Cht5rZj3MsoCjcLrnWDDaxHqFCOwIh2VD5UT5xoy2xcKKpoMAvYe4-kH0xVw8vdaEkGRva0OF1WdfmvoPifSLQLOK4RAGPO72WQifQ87qsF8APOnzvPA3M5LAhp7wvYU8X7f__vZO7Oae4ZVj0dARrF8fms6KVQ__ect74q1YyqECYIjJci7DQkQ?width=2041&height=1334&cropmode=none)




_______________


Another way is the BFS approach from [educative](https://www.educative.io/courses/grokking-the-coding-interview/gx2OqlvEnWG)




```

Given set: [1, 5, 3]

Start with an empty set: [[]]
Add the first number (1) to all the existing subsets to create new subsets: [[], [1]];
Add the second number (5) to all the existing subsets: [[], [1], [5], [1,5]];
Add the third number (3) to all the existing subsets: [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]].

```


{% highlight python %}

def find_subsets(nums):
  subsets = []
  # start by adding the empty subset
  subsets.append([])
  for currentNumber in nums:
    # we will take all existing subsets and insert the current number in them to create new subsets
    n = len(subsets)
    for i in range(n):
      # create a new subset from the existing subset and insert the current element to it
      set = list(subsets[i])
      set.append(currentNumber)
      subsets.append(set)

  return subsets

{% endhighlight %}


Time and space complexity is O(2^n) because we will have 2^n items

