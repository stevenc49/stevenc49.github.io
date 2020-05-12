---
layout: page
title:  Deepest Leaves Sum (BFS)
---




{% highlight python %}

class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None


def deepestLeavesSum(root):

    q = [root]
    level = 0
    hashmap = {}

    while q:

        level_size = len(q)
        
        for i in reversed( range( level_size ) ):

            node = q.pop(0)    

            if level not in hashmap:
                hashmap[level] = [node.val]
            else:
                list = hashmap[level]
                list.append(node.val)
                hashmap[level] = list
            
            # print node.val, level

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        level += 1

    # print hashmap
    # print max(hashmap)
    # list = hashmap[max(hashmap)]
    # print sum(list)
    return sum( hashmap[max(hashmap)] )

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

print deepestLeavesSum(root)

{% endhighlight %}


