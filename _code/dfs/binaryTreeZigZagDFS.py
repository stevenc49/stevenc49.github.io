class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

def zigzagLevelOrder(root):
    
    output = []
    
    def dfs(node, level, output):
        
        if not node:
            return
        
        if len(output) <= level:
            output += [[]]
            
        dfs(node.left, level+1, output)
        dfs(node.right, level+1, output)
        
        if level%2==0:
            output[level].append(node.val)
        else:
            output[level].insert(0, node.val)
    
    dfs(root, 0, output)
    return output


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print( zigzagLevelOrder(root) )