---
layout: page
title:  Insert Interval
last_solved: 2020-06-03
category: intervals
leetcode_url: https://leetcode.com/problems/merge-intervals/
status: Attempted
---

###### Problem:

```
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

###### Solution:

You could insert the new interval into the intervals list and re-sort them but that would make it o(n*logn)

Since the list is already sorted, we can make it linear time but merging the new interval only when it's time to add it to the `merged` output array.

{% highlight python %}


    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = []
        i=0
        
        # add all intervals that come before newInterval
        while i<len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i+=1
        
        
        # merge intervals that overlap with newInterval
        while i<len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min( intervals[i][0], newInterval[0] )
            newInterval[1] = max( intervals[i][1], newInterval[1] )
            i+=1
        
        merged.append(newInterval)
        
        
        # add the remaining intervals to output
        while i<len(intervals):
            merged.append( intervals[i] )
            i+=1
        
        return merged


{% endhighlight %}



