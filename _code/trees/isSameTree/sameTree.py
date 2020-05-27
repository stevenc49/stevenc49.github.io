class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None



def sameTree(p, q):

    if not p and not q:
        return True

    elif p and not q:
        return False
    
    elif not p and q:
        return False
    
    else:

        return p.val==q.val and sameTree(p.left, q.left) and sameTree(p.right, q.right)
            