class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def levelOrder(root):

    q = [root]
    ans = []
    
    
    while q:
        
        level_size = len(q)
        level = []
        
        for i in range(level_size):
            
            curr = q.pop(0)

            level.append(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    
        if level:
            ans.append(level)
    
    return ans[::-1]

    # q = [root]
    # ans = []

    # while q:

    #     level_size = len(q)
    #     level = []

    #     for _ in range(level_size):

    #         curr = q.pop(0)
    #         level.append(curr.val)

    #         if curr.left:
    #             q.append(curr.left)
    #         if curr.right:
    #             q.append(curr.right)
    
    #     ans.append(level)

    # return ans[::-1]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(8)

print( levelOrder(root) )