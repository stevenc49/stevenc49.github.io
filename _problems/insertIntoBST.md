---
layout: page
title:  Insert into BST
last_solved: 
category: tree
leetcode_url: https://leetcode.com/problems/insert-into-a-binary-search-tree
status: Attempted
---

Problem
-------

```
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \   
    1   3
         \
          4
```

Solution
----------



{% highlight python %}

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return TreeNode(val)
        
        # root is bigger, it goes on left side
        if root.val > val:
            
            if not root.left:
                
                root.left = TreeNode(val)
            
            else:
                
                self.insertIntoBST(root.left, val)
        
        
        else:
            
            if not root.right:
                
                root.right = TreeNode(val)
            
            else:
                
                self.insertIntoBST(root.right, val)
        
        return root


{% endhighlight %}

______________



{% highlight python %}


{% endhighlight %}

![image1]()