class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def isSameTree(p, q):

    if not p and not q:
        return True
    
    # both null already covered above
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
 
    leftRes = isSameTree(p.left, q.left)
    rightRes = isSameTree(p.right, q.right)

    return leftRes and rightRes


# def isSameTree(p,q):
#     if p and q:
#         return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
#     return p is q


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

p = root
q = root2

print p
print q
print isSameTree(p, q)