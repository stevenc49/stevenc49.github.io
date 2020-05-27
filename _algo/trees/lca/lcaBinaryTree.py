class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def lca(root, x, y):

    if not root:
        return None
    
    print(root.val)

    if root.val==x or root.val==y:
        print('returning ' + str(root.val))
        return root

    leftRes = lca(root.left, x, y)
    rightRes = lca(root.right, x, y)

    if not rightRes:
        return leftRes
    if not leftRes:
        return rightRes
    if leftRes and rightRes:
        print('returning ' + str(root.val))
        return root




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print( lca(root, 4, 5).val )