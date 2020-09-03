---
layout: page
title:  Merge Two Binary Trees
last_solved: 
category: trees
leetcode_url: https://leetcode.com/problems/merge-two-binary-trees
status: Attempted
---

Problem
-------

```
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
```

Solution
----------



{% highlight python %}

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def dfs(t1, t2, t3):
            
            # sums up the roots
            t3.val = t1.val + t2.val

            # if only t1 has left child
            if t1.left and not t2.left:
                t3.left = t1.left

            # if only t1 has right child
            if t1.right and not t2.right:
                t3.right = t1.right

            # if only t2 has left child
            if t2.left and not t1.left:
                t3.left = t2.left

            # if only t2 has right child
            if t2.right and not t1.right:
                t3.right = t2.right
        
            # recurse down left if both have left
            if t1.left and t2.left:
                t3.left = TreeNode(0)
                dfs(t1.left, t2.left, t3.left)
        
            if t1.right and t2.right:
                t3.right = TreeNode(0)
                dfs(t1.right, t2.right, t3.right)
            
        
        # start of main
        if not t1 and not t2:
            return
        
        if t1 and not t2:
            return t1
        if t2 and not t1:
            return t2
        
        # if t1 and t2
        t3 = TreeNode(0)
        dfs(t1, t2, t3)
        
        return t3
        

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()