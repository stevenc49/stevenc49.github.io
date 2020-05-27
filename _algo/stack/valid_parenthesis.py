
def main():

    str = "([{{}])"

    roundStack = []
    squareStack = []
    curlyStack = []

    # push all to stack
    for i in range(0, len(str)):

        char = str[i]

        if char == "(":
            roundStack.append("(")
        elif char == "[":
            squareStack.append("[")
        elif char == "{":
            curlyStack.append("{")

    # iterate str backwards
    for char in reversed(str):

        if char == ")":
            roundStack.pop()
        elif char == "]":
            squareStack.pop()
        elif char == "}":
            curlyStack.pop()


    if not roundStack and not squareStack and not curlyStack:
        print 'parenthese are valid'
    else:
        print 'parenthese are NOT valid'

if __name__ == "__main__":
    main()
