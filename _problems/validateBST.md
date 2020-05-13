---
layout: page
title:  Validate BST
---


Unfortunately, we can't just check BST conditions for current node and dfs recurse downward. In the following example, node 15 satisfies the condition locally in its subtree (15,6,20) but it has a '6' that is in the root's right subtree (violates the right subtree condition).

{% highlight text %}
# #        10
# #       5 15
# #     X X 6 20
{% endhighlight %}

Wrong way to do it:

{% highlight python %}

class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def validateBST(root):

    if not root:
        return True

    # check BST conditions for current node
    validBST = True

    if root.left and not root.left.val < root.val:
        validBST = False
    
    if root.right and not root.right.val > root.val:
        validBST = False

    leftRes = validateBST(root.left)
    rightRes = validateBST(root.right)

    return validBST and leftRes and rightRes

# #        5
# #       3 7
# #     2 4 6 8

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(7)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(8)



print(validateBST(root))

{% endhighlight %}


The solution to this is to pass down lower and upper limits with each recursive call.

{% highlight text %}

class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def validateBST(root):

    if not root:
        return True
    
    def helper(node, lower, upper):

        if not node:
            return True

        if node.val<=lower or node.val>=upper:    # current node violates left and right conditions
            return False
        
        leftValid = helper(node.left, lower, node.val)
        rightValid = helper(node.right, node.val, upper)

        return leftValid and rightValid
    
    return helper(root, -9999, 9999)


# [10,5,15,null,null,6,20]

#        10
#       5 15
#     X X 6 20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)


print(validateBST(root))

{% endhighlight %}


![image1]()