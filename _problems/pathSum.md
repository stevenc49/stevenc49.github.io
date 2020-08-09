---
layout: page
title:  Path Sum
last_solved: 
category: 
leetcode_url: https://leetcode.com/problems/path-sum
status: Attempted
---

Problem
-------

```
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

```

Solution
----------

Use dfs helper to pass down currentSum. Check if leaf node and sumTotal==targetSum.

{% highlight python %}

def hasPathSum(self, root, sum):

    if not root:
        return False

    def dfs(node, currentSum, targetSum):
        
        # if current node is leaf and sum of all vals == targetSum
        if node.left is None and node.right is None and currentSum + node.val == targetSum:
            return True

        leftRes = dfs(node.left, currentSum + node.val, targetSum)
        rightRes = dfs(node.right, currentSum + node.val, targetSum)

        return leftRes or rightRes

    return dfs(root, 0, sum)

{% endhighlight %}

_______________



{% highlight python %}

def dfs(root, sum):
    
    if not root:
        return False
    
    # if the current node is a leaf and it's value is equal to the sum, we found a path
    if root.val==sum and root.left is None and root.right is None:
        return True
    
    # recursively call to traverse the left and right sub-tree
    # return true if any of the two recursive call return true
    leftRes = dfs(root.left, sum-root.val)
    rightRes = dfs(root.right, sum-root.val)
    
    return leftRes or rightRes

return dfs(root, sum)


{% endhighlight %}


![image1](https://5wkfbq.dm.files.1drv.com/y4m1LAF1rJH3rvE6Fvoa19b9yQaMDbSKWiaK30lMziT7NLyxl8pZnpAV9b8fA4kYg-9pbglZXrlKtwQ6m57t3x1Eup0UAeaUw2l8He8myjMvgvUpiOVvhQD9Tr_5i5mw3hLqErN-otBc4QQanjNm0ye7UiqB-b8ymiORnOz7TAHQLWcHuuZR5k0Can1XRKt846BNzH5OzeZbTMuifNt2NXGbQ?width=1477&height=2053&cropmode=none)