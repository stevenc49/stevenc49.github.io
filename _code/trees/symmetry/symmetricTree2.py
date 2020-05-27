class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def isSymmetric(root):

    def isMirror(left, right):
        
        if not left and not right:
            return True

        if left and not right:
            return False

        if right and not left:
            return False

        if left and right and left.val == right.val:
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return False

    if not root:
        return True
    
    return isMirror(root.left, root.right)


root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)


print(isSymmetric(root))