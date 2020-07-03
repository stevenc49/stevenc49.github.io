n=3

def generateParenthesis(n):
    
    def backtrack(outputList, currentString, open, close, n):

        if len(currentString)==2*n:
            outputList.append(currentString)
            print("output " + currentString)
            return

        print( currentString )

        if open < n:
            backtrack( outputList, currentString+"(", open+1, close, n )

        if close < open:
            backtrack( outputList, currentString+")", open, close+1, n)
            
    outputList = []
    backtrack(  outputList, "", 0, 0, n)
    return outputList
        

print( generateParenthesis(n) )