
class MinStack:

    def __init__(self):

        self.s1 = []
        self.s2 = []


    def push(self, num):

        self.s1.append( num )

        if len(self.s2)==0 or num < self.s2[-1]:
            self.s2.append( num )
        else:
            self.s2.append( self.s2[-1] )


    def pop(self):

        self.s2.pop()

        return self.s1.pop()


    def show(self):

        print(self.s1)
        print(self.s2)
        print("Min: ", self.s2[-1] )
        print('')

def main():

    minStack = MinStack()

    minStack.push(3)
    minStack.show()

    minStack.push(1)
    minStack.show()

    minStack.push(2)
    minStack.show()
    
    minStack.pop()
    minStack.show()

    minStack.pop()
    minStack.show()

if __name__ == "__main__":
    main()
