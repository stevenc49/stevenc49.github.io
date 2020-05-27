s = "]"


def isValid(s):

    open_list = ["(", "{", "["]
    close_list = [")", "}", "]"]


    stack=[]

    for i in range(0, len(s)):

        char = s[i]

        if char in open_list:
            stack.append(char)
        elif char in close_list:

            # find index of closing char
            index = close_list.index(char)
            matching_open_char = open_list[index]

            if stack and stack[-1]==matching_open_char:
                stack.pop()
            else:
                return False      # in case str="]"
        
    if not stack:
        return True
    else:
        return False


print isValid(s)