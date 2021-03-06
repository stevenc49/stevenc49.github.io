---
layout: page
title:  Sum Root to Leaf Numbers
last_solved: 2020-06-26
category: trees
leetcode_url: https://leetcode.com/problems/sum-root-to-leaf-numbers
status: Attempted
---

Problem
-------

```
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

```

Solution
----------

{% highlight python %}

def sumNumbers(root):

    if not root: return 0
    
    output = []     # list of strings of each path: ["12", "13"]
    
    def dfs(root, sofar):   # sofar is list of integers as we recurse down the tree
        
        if root.left is None and root.right is None:
            output.append("".join(sofar+[str(root.val)]))
            
        if root.left:
            # sofar.append(str(root.val))
            dfs(root.left, sofar+[str(root.val)])
        
        if root.right:
            # sofar.append(str(root.val))
            dfs(root.right, sofar+[str(root.val)])

    dfs(root, [])
    
    return sum([ int(x) for x in output ])

{% endhighlight %}


_____________


Anotehr solution


{% highlight python %}

def sumNumbers(self, root: TreeNode) -> int:

    def dfs(root, n):
        if not root:
            return 0
        n = n*10 + root.val
        if not root.left and not root.right:
            return n
        else:
            return dfs(root.left, n) + dfs(root.right, n)
    return dfs(root, 0)


{% endhighlight %}


![image1](https://5wjpjg.dm.files.1drv.com/y4mQXn_k4mYsnwW7OsyfFTgPp4V0-G1X9AvuveNRV_HZ72gpClN9TsNQGqUSULWOT_SKWwlYsXBCT6U117kb5dUfFA7AljA3iQiTDr2F_1d7jWuXB1vSz7Pa6B1NgFvapoHBQ48y1F5-_sBTG7O1ZIjo9g3xc8-suiyyCTjaMKYL5x-jCLtp9LvCHGTW9s9LzreX4okmXD7StEu6vDLbF4DYw?width=1400&height=2901&cropmode=none)