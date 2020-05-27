
class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def serialize(root):

    if not root:
        return "X"

    leftSerialized = serialize(root.left)
    rightSerialized = serialize(root.right)

    return str(root.val) + leftSerialized + rightSerialized



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)


print serialize(root)

