
def main():

    str = "(]"

    stack = []

    for i in range(0, len(str)):

        char = str[i]

        if char=="(" or char=="[" or char=="{":
            stack.append(char)
        elif char==")" or char=="]" or char=="}":
            stack.pop()
    
    if not stack:
        print 'parenthese are valid'
    else:
        print 'parenthese are NOT valid'

if __name__ == "__main__":
    main()
