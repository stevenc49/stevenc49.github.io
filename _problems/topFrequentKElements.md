---
layout: page
title:  Top Frequent K Elements
last_solved: 2020-07-17
category: heap
leetcode_url: https://leetcode.com/problems/top-k-frequent-elements/solution/
status: Attempted
---

Problem
-------

```
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

```

Solution
----------

Two ways to solve this. Both involve heapq library

{% highlight python %}

from collections import Counter
import heapq

nums = [1,1,1,2,2,3]

def topKFrequent1(nums, k):

    count = Counter(nums)

    return heapq.nlargest(k, count.keys(), key=count.get) 


def topKFrequent2(nums, k):

    c = Counter(nums)   # {1: 3, 2: 2, 3: 1}


    c = [(-v,k) for k,v in c.items()]    # (v,k)  [(3, 1), (2, 2), (1, 3)]
                                         # (-v,k) [(-3, 1), (-2, 2), (-1, 3)]
    
    heapq.heapify(c)

    output = []
    for i in range(k):
        item = heapq.heappop(c)
        output.append(item[1])
    
    return output


print(topKFrequent2(nums, 2))

{% endhighlight %}


![image1]()