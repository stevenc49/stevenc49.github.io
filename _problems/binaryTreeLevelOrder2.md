---
layout: page
title:  Binary Tree Level Order Traversal II
last_solved: 2020-07-01
category: bfs
leetcode_url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
status: Not Solved
---

Problem
-------

```
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

```

Solution
----------

Got the wrong answer even though it seems like I've been doing the same in the past. Review it tmr.

```
Your input
[3,9,20,null,null,15,7]
Output
[[15,9],[20,7],[3]]
Expected
[[15,7],[9,20],[3]]
```

{% highlight python %}

def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        q = [root]
        ans = []
        
        
        while q:
            
            level_size = len(q)
            level = []
            
            for i in range(level_size):
                
                curr = q.pop()

                if curr:
                
                    level.append(curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
        
            if level:
                ans.append(level)
        
        return ans[::-1]

{% endhighlight %}


![image1]()