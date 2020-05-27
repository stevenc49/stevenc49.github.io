class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def levelOrder(root):

    q = [root]
    level = 0

    while q:

        level_size = len(q)

        for i in range(level_size):

            curr = q.pop(0)
            print(curr.val, level)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    
        level += 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

levelOrder(root)