---
layout: page
title:  Max Depth of Tree
---




{% highlight python %}


class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def deepestNode(root, level, maxLevel):

    if not root:
        return maxLevel

    if level > maxLevel:
        maxLevel = level
    

    leftRes = deepestNode(root.left, level + 1, maxLevel)
    rightRes = deepestNode(root.right, level + 1, maxLevel)


    if leftRes and rightRes:
        return max(leftRes, rightRes)



root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)



print deepestNode(root, 1, 0)


{% endhighlight %}


![image1](https://bubblesortblog.files.wordpress.com/2020/03/img_20200331_164909.jpg?w=768)