class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None


def isSubTree(s, t):

    if not s:
        return False
    if isSameTree(s, t):
        return True
    return isSubTree(s.left, t) or isSubTree(s.right, t)



def isSameTree(p, q):

    if p and q:
        return p.val==q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return p is q



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

p = root
q = root2

print isSubTree(p, q)