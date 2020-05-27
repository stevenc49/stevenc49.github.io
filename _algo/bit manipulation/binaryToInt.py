
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None




def getCount(head):

    count = 0
    while head:
        count = count + 1
        head = head.next
    return count


def binToInt(head):

    sum = 0
    count = getCount(head) - 1

    while head:
        sum = sum + ( (2**count) * head.val )
        count = count-1
        head = head.next
    
    return sum


head = Node(1)
head.next = Node(0)
head.next.next = Node(1)

print( getCount(head) )
print( binToInt(head) )