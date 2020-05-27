
class TreeNode:

    def __init__(self, val):

        self.val = val
        self.left = None
        self.right = None

'''

'''
def deserialize(nodesLeft):

    # treat nodesLeft like a queue of incoming nodes to be serialized
    char = nodesLeft.pop(0)

    if char=='X':
        return None

    n = TreeNode(char)
    n.left = deserialize(nodesLeft)
    n.right = deserialize(nodesLeft)

    return n



# serialized = "1,2,3,X,X,X,X"
# serialized = "1,2,X,X,3,4,X,X,5,X,X"
serialized = "3,9,20,X,X,15,7"

nodesLeft = serialized.split(",")   # a helper fuction can do this
n = deserialize( nodesLeft )        # this is the actual recursive call

print n.val
print n.left.val
print n.right.val
print n.right.left.val
print n.right.right.val

# split = serialized.split(",")

# print( split.pop(0) )
# print( split.pop(0) )
# print( split.pop(0) )
