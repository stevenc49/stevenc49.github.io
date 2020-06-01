---
layout: page
title:  invert Tree
last_solved: 2020-06-01
category: tree
leetcode_url: https://leetcode.com/problems/invert-binary-tree/
status: Solved
---




{% highlight python %}

class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def invert(root):

    if not root:
        return

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert(root.left)
    invert(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)


print( root.left.left.val ) # 4

{% endhighlight %}


![image1]()