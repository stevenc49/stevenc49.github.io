
class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

'''

'''
def printKdistance(root, k):

    if k==0:
        print( root.val )
        return
    
    printKdistance(root.left, k-1)
    printKdistance(root.right, k-1)





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

printKdistance(root, 1)

