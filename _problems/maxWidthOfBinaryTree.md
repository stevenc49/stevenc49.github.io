---
layout: page
title:  Max Width of Binary Tree
last_solved: 2020-07-09
category: trees
leetcode_url: https://leetcode.com/problems/maximum-width-of-binary-tree
status: Solved
---

Problem
-------

```
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


```

Solution
----------

Tried this but it fails on some test cases.

{% highlight python %}

def widthOfBinaryTree(self, root: TreeNode) -> int:
    
    q = [(root, 0)]
    maxWidth = 0
    
    while q:
        
        lvl = []
        lvl_size = len(q)
                    
        for _ in range(lvl_size):
            
            maxWidth = max(maxWidth, q[-1][1]-q[0][1]+1 )
            
            node, num = q.pop(0)
            lvl.append( (node.val, num)  )
        
            
            if node.left:
                q.append( (node.left, 2*num) )
            if node.right:
                q.append( (node.right, 2*num+1))
        
        
        print(lvl, maxWidth)
    
    return maxWidth

{% endhighlight %}

```
Your input
[1,3,2,5,3,null,9]

stdout
[(1, 0)] 1
[(3, 0), (2, 1)] 2
[(5, 0), (3, 1), (9, 3)] 4

```


__________

The one works. Check the difference.

{% highlight python %}

def widthOfBinaryTree(self, root: TreeNode) -> int:
    
    q = [(root, 0)]
    maxWidth = 0
    
    while q:

        new_lvl = []
        lvl_size = len(q)
                    
        for _ in range(lvl_size):
            
            maxWidth = max(maxWidth, q[-1][1]-q[0][1]+1 )
            
            node, num = q.pop(0)
            # new_lvl.append( (node, num) )
        
            if node.left:
                new_lvl.append( (node.left, 2*num) )
            if node.right:
                new_lvl.append( (node.right, 2*num+1))
        
        q = new_lvl     # need to "reset" the nums so the left most is zero again
    
    return maxWidth

{% endhighlight %}

![image1]()