class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):

    if not root: return 0
    
    output = []     # list of strings of each path: ["12", "13"]
    
    def dfs(root, sofar):   # sofar is list of integers as we recurse down the tree
        
        if root.left is None and root.right is None:
            output.append("".join(sofar+[str(root.val)]))
            
        if root.left:
            # sofar.append(str(root.val))
            dfs(root.left, sofar+[str(root.val)])
        
        if root.right:
            # sofar.append(str(root.val))
            dfs(root.right, sofar+[str(root.val)])

    dfs(root, [])
    
    return sum([ int(x) for x in output ])


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print( sumNumbers(root) )