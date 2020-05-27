class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None


def deepestLeavesSum(root):

    levelMap = dict()

    def dfs(root, level):

        if not root:
            return
        
        # add val to the levelMap
        levelMap[level] = root.val + levelMap.get(level, 0)
    
        dfs(root.left, level+1)
        dfs(root.right, level+1)

    dfs(root, 0)
    print(levelMap)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

deepestLeavesSum(root)
