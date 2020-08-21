---
layout: page
title:  Longest Univar Path
last_solved: 
category: tree
leetcode_url: https://leetcode.com/problems/longest-univalue-path/
status: Not Solved
---

Problem
-------

```

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5

```

Solution
----------

This is not solved. Gotten close but fails some test cases

{% highlight python %}

    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        def dfs2(node, currentLongest):
            
            if not node: return currentLongest
            
            if node.left:
                if node.val==node.left.val:
                    currentLongest+=1
                else:
                    currentLongest=0
            
            
            if node.right:
                if node.val==node.right.val:
                    currentLongest+=1
                else:
                    currentLongest=0
            
            leftRes = dfs2(node.left, currentLongest)
            rightRes = dfs2(node.right, currentLongest)
            
            return max(leftRes, rightRes)
        
        
        return dfs2(root, 0)

{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()