---
layout: page
title:  Path Sum 2
last_solved: 
category: tree
leetcode_url: https://leetcode.com/problems/path-sum-ii/
status: Attempted
---

Problem
-------

```
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

```

Solution
----------

Use dfs helper to pass down currentSum. Check if leaf node and sumTotal==targetSum.

{% highlight python %}

        def dfs(node, currentSum, targetSum, path):

            if not node:
                return
            
            # if current node is leaf and sum of all vals == targetSum
            if node.left is None and node.right is None and currentSum + node.val == targetSum:
                output.append(path+[node.val])

            leftRes = dfs(node.left, currentSum + node.val, targetSum, path+[node.val])
            rightRes = dfs(node.right, currentSum + node.val, targetSum, path+[node.val])

            return

        output = []
        dfs(root, 0, sum, [])
        return output

{% endhighlight %}

_______________

{% highlight python %}



{% endhighlight %}