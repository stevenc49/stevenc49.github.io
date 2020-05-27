class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def validateBST(root):

    if not root:
        return True
    
    def helper(node, lower, upper):

        if not node:
            return True

        if node.val<=lower or node.val>=upper:    # current node violates left and right conditions
            return False
        
        leftValid = helper(node.left, lower, node.val)
        rightValid = helper(node.right, node.val, upper)

        return leftValid and rightValid
    
    return helper(root, float('-inf'), float('inf'))

# #        5
# #       3 7
# #     2 4 6 8

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(7)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(8)


# [10,5,15,null,null,6,20]

#        10
#       5 15
#     X X 6 20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)


print(validateBST(root))