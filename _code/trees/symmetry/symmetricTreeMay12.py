class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def isSymmetric(root):

    if not root:
        return True

    def isMirror(p, q):

        if not p and not q:
            return True
        
        if (p and not q) and (not p and q):
            return False

        if p and q and p.val==q.val and isMirror(p.left, q.right) and isMirror(p.right, q.left):
            return True
        
        return False

    return isMirror(root.left, root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)


print(isSymmetric(root))