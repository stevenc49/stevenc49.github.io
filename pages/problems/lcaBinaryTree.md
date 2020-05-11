---
layout: page
title:  LCA of binary tree
---




{% highlight python %}

class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def lca(root, x, y):

    if not root:
        return None
    
    print(root.val)

    if root.val==x or root.val==y:
        print('returning ' + str(root.val))
        return root

    leftRes = lca(root.left, x, y)
    rightRes = lca(root.right, x, y)

    if not rightRes:
        return leftRes
    if not leftRes:
        return rightRes
    if leftRes and rightRes:
        print('returning ' + str(root.val))
        return root




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print( lca(root, 4, 5).val )

{% endhighlight %}


![image1](https://srmuba.dm.files.1drv.com/y4mjQ4fvTsdlacL5xumNsVzQqLEDQaxCFdrXcoyJFTs9aqCCJWjMr8jJaYvkOIg12cpO1JtFD1giwPbygRfq0ju1TYMXTJzfSYpxVMFBwUebhp3vhzJw_3bF7Qxp2DzfE2usG5kjMmQYJnMWKJZAmATlnhkev2N9oJa_glDY_UTZxfmytLPepbwK4vYmUblwg3hpVOyX-6596pfhNFGESWB0w?width=1824&height=2225&cropmode=none)