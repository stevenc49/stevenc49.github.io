class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None




def sumEvenGrandparent(root):

    sum = 0      # global var

    def dfs(root, sum):
    
        if not root:
            return 0

        # moving recursive calls up here (making this postorder instead of preorder) and adding sum = make this work
        if root.left:
            sum = dfs(root.left, sum)
        if root.right:
            sum = dfs(root.right, sum)

        if root.val % 2 == 0:

            if root.left and root.left.left:
                print( "even grandparent is %s" % root.val  )
                print( "sum " + str(sum) + " adding " + str(root.left.left.val))
                sum = sum + root.left.left.val
                
            
            if root.left and root.left.right:
                print( "even grandparent is %s" % root.val  )
                print( "sum " + str(sum) + " adding " + str(root.left.right.val))
                sum = sum + root.left.right.val
                

            if root.right and root.right.left:
                print( "even grandparent is %s" % root.val  )
                print( "sum " + str(sum) + " adding " + str(root.right.left.val))
                sum = sum + root.right.left.val
                

            if root.right and root.right.right:
                print( "even grandparent is %s" % root.val  )
                print( "sum " + str(sum) + " adding " + str(root.right.right.val))
                sum = sum + root.right.right.val
        
        # dfs(root.left, sum)
        # dfs(root.right, sum)

        return sum

    # call inner function
    return dfs(root, sum)

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
# root.left.left = TreeNode(9)
# root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

print( sumEvenGrandparent(root) )