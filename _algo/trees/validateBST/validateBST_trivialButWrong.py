class TreeNode:
 
    def __init__(self, val):
 
        self.val = val
        self.left = None
        self.right = None



def validateBST(root):

    if not root:
        return True

    # check BST conditions for current node
    validBST = True

    if root.left and not root.left.val < root.val:
        validBST = False
    
    if root.right and not root.right.val > root.val:
        validBST = False

    leftRes = validateBST(root.left)
    rightRes = validateBST(root.right)

    return validBST and leftRes and rightRes

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

# #        10
# #       5 15
# #     X X 6 20

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)


print(validateBST(root))