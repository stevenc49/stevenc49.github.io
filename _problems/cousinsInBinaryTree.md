---
layout: page
title:  Cousins in Binary Tree
last_solved: 
category: bfs, dfs
leetcode_url: https://leetcode.com/problems/cousins-in-binary-tree
status: Solved
---

Problem
-------

```
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

```

![image1](https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png)

Solution
----------

BFS

{% highlight python %}

def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    
    if not root:
        return []
    
    q = [root]
    parents = defaultdict(list) # track parents in a dictionary
    levels = []
    
    
    parents[root.val] = None
    
    while q:

        level = []
        
        for _ in range(len(q)):
        
            curr = q.pop(0)
            level.append(curr.val)
        
            if curr.left:
                q.append(curr.left)
                parents[curr.left.val] = curr.val
            
            
            if curr.right:
                q.append(curr.right)
                parents[curr.right.val] = curr.val
    
        levels.append(level)
    
    print(levels)
    print(parents)
    
    
    # loop thru rows and check if they have different parents
    for row in levels:
        if x in row and y in row and parents[x] != parents[y]:
            return True
    
    return False

{% endhighlight %}

______________

DFS

[How does this work with self](https://leetcode.com/problems/cousins-in-binary-tree/discuss/741717/Python-beats-98-(easy-to-understand)-with-explanation)

Note: use `self.xxx` instead of `nonlocal`

{% highlight python %}

def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    
    def dfs(node, level, parent):
        
        if not node:
            return
        
        if node.val == x:
            self.x_level = level
            self.x_parent = parent
        elif node.val == y:
            self.y_level = level
            self.y_parent = parent

        dfs(node.left, level+1, node)
        dfs(node.right, level+1, node)


    dfs(root, 0, None)

    return self.x_level==self.y_level and self.x_parent!=self.y_parent

{% endhighlight %}