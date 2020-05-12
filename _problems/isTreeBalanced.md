---
layout: page
title:  Is Tree Balanced?
---




{% highlight python %}

class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

'''
    A tree is balanced if the height of the left and right subtrees do not differ by more than 1


    two approaches given by: https://www.youtube.com/watch?v=LU4fGD-fgJQ
    this is approach #1 (inefficient because all nodes will call the height() function)
'''
def isTreeBalanced(root):

    if not root:
        return True
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    if abs( leftHeight - rightHeight ) <= 1 and isTreeBalanced(root.left) and isTreeBalanced(root.right):
        return True
    
    return False


'''
    this is the function to get height of any node
'''
def height(root):

    if not root:
        return 1
    else:
        return 1 + max( height(root.left), height(root.right) )


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(20)
# root.right.right.right = TreeNode(20)

print( isTreeBalanced(root) )


{% endhighlight %}


