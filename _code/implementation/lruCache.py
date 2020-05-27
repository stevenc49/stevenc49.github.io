
class DLLNode:

    def __init__(self, key, val):

        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LruCache:

    def __init__(self, capacity):

        # hashtable for fast lookup
        self.hashmap = {}
        self.capacity = capacity

        self.head = None     # most recently used item
        self.tail = None     # least recently used item


    def get(self, key):

        ## TODO

        return hashmap.get(key)
    
    '''
        put will need to put elements into 
    '''
    def put(self, key, val):

        # if capacity is reached, evict last elem
        # if len(self.hashmap)==self.capacity:

        #     print "capacity reached"
        #     lastNode = self.tail
        #     self.tail = lastNode.prev
        #     lastNode.prev = None

            

        # key exists in hash table
        if key in self.hashmap:

            # update node's value
            currentNode = self.hashmap[key]
            currentNode.val = val
            
            # if current node is not head
            if not currentNode == self.head:

                # remove yourself from list
                if currentNode.prev:
                    currentNode.prev.next = currentNode.next
                if currentNode.next:
                    currentNode.next.prev = currentNode.prev

                # add to beginning of list
                currentNode.next = self.head
                self.head = currentNode         # reassign head node

            # if current node is tail node
            if currentNode == self.tail:
                self.tail = currentNode.prev
                currentNode.prev = None
                



        # not in hash table
        else:

            # put it at the front of the list
            newNode = DLLNode(key, val)
            
            if not self.head:
                self.head = newNode
                self.tail = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode          # reassign head node


            # add node to hash table
            self.hashmap[key] = newNode

    def show(self):

        # print hashmap
        print( self.hashmap )
        print ("head: " + str(self.head.val))
        print ("tail: " + str(self.tail.val))

        # iterate doubly linked list
        node = self.head
        while node:
            print( node.val )
            node = node.next

        print("")
        




cache = LruCache(3)
cache.put(1,10)
cache.put(2,20)
cache.put(3,30)
cache.show()


cache.put(2, 200)     # move elem to head
cache.show()

cache.put(1, 100)       # move end elem to beginning
cache.show()

cache.put(1, 1000)     # move start elem to beginning (breaks)
cache.show()

cache.put(4, 40)
cache.show()            # test new eviction logic
