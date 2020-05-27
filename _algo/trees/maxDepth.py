
class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


'''
    https://leetcode.com/submissions/detail/48266023/
'''
def maxDepth(root):

    if not root:
        return 0
    else:
        return 1 + max( maxDepth(root.left), maxDepth(root.right) )


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
#root.right.right.right = TreeNode(5)



print maxDepth(root)
