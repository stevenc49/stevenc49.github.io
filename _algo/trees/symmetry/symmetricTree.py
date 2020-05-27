class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def isSymmetric(root):

    if not root:
        return True

    # no child nodes
    if not root.left and not root.right:
        return True
    # only left exists
    elif root.left and not root.right:
        return False
    # only right exists
    elif not root.left and root.right:
        return False
    # both exists
    if root.left.val == root.right.val:
        return True

    if root.left:
        leftRes = isSymmetric(root.left)
    if root.right:
        rightRes = isSymmetric(root.right)
    
    return leftRes and rightRes




root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)


print(isSymmetric(root))