n=3

def generateParenthesis(n):
    
    def backtrack(outputList, currentString, open, close, max):

        if len(currentString)==2*max:
            outputList.append(currentString)
            return
        

        if open < max:
            backtrack( outputList, currentString+"(", open+1, close, max )

        if close < open:
            backtrack( outputList, currentString+")", open, close+1, max)
            
    outputList = []
    backtrack(  outputList, "", 0, 0, n)
    return outputList
        

print( generateParenthesis(n) )