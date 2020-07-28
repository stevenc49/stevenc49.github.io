---
layout: page
title:  Last Stone Weight
last_solved: 
category: 
leetcode_url: https://leetcode.com/problems/last-stone-weight
status: Attempted
---

Problem
-------

```
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

```

Solution
----------

{% highlight python %}

def lastStoneWeight(self, stones: List[int]) -> int:

    while len(stones)>=2:

        # negate values for max heap
        stones = list(map(lambda x: -x if x>0 else x, stones))
        # stones = [-x for x in stones if x>0 else x]
        print(stones)

        # get top 2 heaviest stones
        heapq.heapify(stones)
        print(stones)
        heavy1 = heapq.heappop(stones)
        heavy2 = heapq.heappop(stones)

        # smash the heaviest stones
        diff = abs(heavy1-heavy2)
        heapq.heappush(stones, diff)
        print(stones)

    print(stones)
    return stones[0]

{% endhighlight %}


![image1]()