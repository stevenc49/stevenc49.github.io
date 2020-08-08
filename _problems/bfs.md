---
layout: page
title:  BFS
---

Time complexity is O(N)
Space complexity is O(W) where W is the max number of nodes on any level.


{% highlight python %}

class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def levelOrder(root):

    queue = []
    queue.append( root )
    levels = []

    while queue:

        level_size = len(queue)
        level = []

        while level_size:

            node = queue.pop(0)

            if node:
                level.append( node.val )

                if node.left:
                    queue.append( node.left )
                if node.right:
                    queue.append( node.right )

            level_size -= 1
        
        if level:
            levels.append( level )
    
    print levels

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
# root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(7)

levelOrder(root)


{% endhighlight %}

