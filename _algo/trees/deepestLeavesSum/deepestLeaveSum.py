class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def deepestLeavesSum(root):

    d = dict()  # keeps track of level:sum

    def dfs(root, level):

        print d

        d[level] = root.val + d.get(level, 0)   # the "0" is the default return value if level is not in dictionary, otherwise None would be returned

        if root.left:
            dfs(root.left, level+1)
        if root.right:
            dfs(root.right, level+1)
    
    dfs(root, 0)
    return d[ max(d) ]  # max() on dictionary gives max key



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

print( deepestLeavesSum(root) )

        