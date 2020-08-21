---
layout: page
title:  Path Sum 3
last_solved: 
category: tree
leetcode_url: https://leetcode.com/problems/path-sum-iii/
status: Attempted
---

Problem
-------

```
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

```

Solution
----------

This is a double nested dfs solution so runtime is horrible but it still works.

{% highlight python %}

    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        self.total = 0
        
        def helper(node, currSum):
            if not node:
                return
            
            helper(node.left, currSum+node.val)
            helper(node.right, currSum+node.val)
        
            if node.val + currSum == sum:
                self.total+=1
        
        
        def dfs(node):
            
            if not node: return
            
            helper(node, 0)
            
            dfs(node.left)
            dfs(node.right)
            
        
        dfs(root)
        
        return self.total

{% endhighlight %}

_______________

{% highlight python %}



{% endhighlight %}