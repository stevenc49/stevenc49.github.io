---
layout: page
title:  Binary Tree Zig Zag (DFS)
last_solved: 2020-07-22
category: bfs
leetcode_url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
status: Attempted
---

Problem
-------

```
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
        

```

Solution
----------

{% highlight python %}

def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    
    output = []
    
    def dfs(node, level, output):
        
        if not node:
            return
        
        if len(output) <= level:
            output += [[]]
            
        dfs(node.left, level+1, output)
        dfs(node.right, level+1, output)
        
        if level%2==0:
            output[level].append(node.val)
        else:
            output[level].insert(0, node.val)
    
    dfs(root, 0, output)
    return output
        
{% endhighlight %}


![image1]()