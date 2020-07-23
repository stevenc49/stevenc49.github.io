---
layout: page
title:  Maximum Depth of N-ary Tree
last_solved: 2020-07-23
category: trees
leetcode_url: https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
status: Solved
---

Problem
-------

```
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:

![image1](https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png)

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

```

Solution
----------

{% highlight python %}

def maxDepth(self, root: 'Node') -> int:
    
    if not root:
        return 0
    
    maxDepthAtThisRoot = 0
    if root.children:
        for child in root.children:
            maxDepthAtThisRoot = max(maxDepthAtThisRoot, self.maxDepth(child))
    
    return maxDepthAtThisRoot+1

{% endhighlight %}


