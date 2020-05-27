class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def isSymmetric(root):




root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.right = TreeNode(3)


print(isSymmetric(root))