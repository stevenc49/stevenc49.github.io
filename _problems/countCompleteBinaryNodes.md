---
layout: page
title:  Count Complete Tree Nodes
last_solved: 2020-06-23
category: trees
leetcode_url: https://leetcode.com/problems/count-complete-tree-nodes/
status: Attempted
---

Problem
-------

```
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

```

Solution
----------

There should be a better way to do this than O(n) if you take advantage of the complete binary tree property.

{% highlight python %}

def countNodes(self, root: TreeNode) -> int:
    
    if not root:
        return 0
    
    leftRes = self.countNodes(root.left)
    rightRes = self.countNodes(root.right)
    
    return 1 + leftRes + rightRes

{% endhighlight %}


![image1]()