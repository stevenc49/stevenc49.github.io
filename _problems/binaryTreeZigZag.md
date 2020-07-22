---
layout: page
title:  Binary Tree Zig Zag
last_solved: 2020-07-22
category: bfs
leetcode_url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
status: Solved
---

Problem
-------

```
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return
        
        q = [root]
        ans = []
        odd = True
        
        while q:
            
            level_len = len(q)
            level = []
            
            for _ in range(level_len):
            
                curr = q.pop(0)

                if curr:
                
                    level.append(curr.val)

                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
            if odd:
                ans.append(level)
            else:
                ans.append(reversed(level))
            odd = not odd
        
        return ans
        

```

Solution
----------

{% highlight python %}

def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    
    if not root: return
    
    q = [root]
    ans = []
    odd = True
    
    while q:
        
        level_len = len(q)
        level = []
        
        for _ in range(level_len):
        
            curr = q.pop(0)

            if curr:
            
                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        
        if odd:
            ans.append(level)
        else:
            ans.append(reversed(level))
        odd = not odd
    
    return ans
        
{% endhighlight %}


![image1]()