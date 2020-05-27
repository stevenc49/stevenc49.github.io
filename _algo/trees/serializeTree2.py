
class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None


def serialize(root):

    if not root:
        return "X"
    
    leftRes = serialize(root.left)
    rightRes = serialize(root.right)

    return str(root.val) + "," + leftRes + "," + rightRes


def deserialize(str):

    def dfs(nodesLeftList):

        # treat nodesLeft like a queue of incoming nodes to be serialized
        char = nodesLeftList.pop(0)

        if char=='X':
            return None

        node = TreeNode(char)
        node.left = dfs(nodesLeftList)
        node.right = dfs(nodesLeftList)

        return node

    nodesLeftList = str.split(",")
    n = dfs( nodesLeftList )        # this is the actual recursive call
    return n

print("Serialize..")
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
serialized = serialize(root)
print(serialized)
print()

print("Deserialize..")
root2 = deserialize(serialized)
print( root2.val )
print( root2.left.val )
print( root2.right.val )
print( root2.right.left.val )
print( root2.right.right.val )
