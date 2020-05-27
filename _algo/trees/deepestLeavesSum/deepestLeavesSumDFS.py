class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None


def deepestLeavesSum(root):

    map = {}

    def dfs(root, depth):

        map[depth] = root.val + map.get(depth, 0)

        if root.left:
            dfs(root.left, depth+1)
        if root.right:
            dfs(root.right, depth+1)
        

    dfs(root, 0)
    return map[max(map)]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print deepestLeavesSum(root)