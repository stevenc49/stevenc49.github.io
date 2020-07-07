
s = "bb"

def longestPalindrome(s):

    def expandAroundCenter(s, l, r):
        
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1

        return s[l+1:r]



    res = ""
    for i in range(len(s)):
        oddPalin = expandAroundCenter(s, i, i)
        evenPalin = expandAroundCenter(s, i, i+1)

        print(oddPalin, evenPalin)

        if len(oddPalin)>len(res):
            res = oddPalin
        if len(evenPalin)>len(res):
            res = evenPalin
    
    return res
    
    

    # start, end = 0,0

    # for i in range(len(s)):
    #     len1 = expandAroundCenter(s, i, i)
    #     len2 = expandAroundCenter(s, i, i+1)

    #     print(len1, len2)
    #     length = max(len1, len2)

    #     if length > end-start:
    #         start = i-(length-1)/2
    #         end = i + length/2
    
    # return s[start:end+1]





print(longestPalindrome(s))
