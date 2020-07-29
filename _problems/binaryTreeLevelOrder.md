---
layout: page
title:  Binary Tree Level Order Traversal
last_solved: 2020-07-28
category: bfs
leetcode_url: https://leetcode.com/problems/binary-tree-level-order-traversal
status: Solved
---

Problem
-------

```
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

```

Solution
----------

BFS

{% highlight python %}

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    
    if not root: return []
    
    q = [root]
    output = []
    
    while q:
        
        level = []
        
        for _ in range(len(q)):
        
            curr = q.pop(0)

            if curr:

                level.append(curr.val)

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
    
        output.append(level)
    
    return output

{% endhighlight %}


________________

DFS

{% highlight python %}

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        output = []
        
        def dfs(node, level, output):
        
            if not node:
                return
            
            if len(output) <= level:
                output += [[]]      # or output.append([])
            
            dfs(node.left, level+1, output)
            dfs(node.right, level+1, output)
            
            output[level].append(node.val)

        dfs(root, 0, output)
        return output


{% endhighlight %}

![image1]()