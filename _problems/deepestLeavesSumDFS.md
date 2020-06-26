---
layout: page
title:  Deepest Leaves Sum (DFS)
last_solved: 2020-06-25
category: trees
leetcode_url: https://leetcode.com/problems/deepest-leaves-sum/
status: Solved
---

```
Given a binary tree, return the sum of values of its deepest leaves.
```


{% highlight python %}

class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None


def deepestLeavesSum(root):

    map = {}

    def dfs(root, depth):

        map[depth] = root.val + map.get(depth, 0)

        if root.left:
            dfs(root.left, depth+1)
        if root.right:
            dfs(root.right, depth+1)
        

    dfs(root, 0)
    return map[max(map)]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print deepestLeavesSum(root)

{% endhighlight %}


![image1]()