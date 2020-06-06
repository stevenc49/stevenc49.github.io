strs = ["flower","flow","flight"]
strs = ["c","acc","ccc"]


'''
'''
def lcp(strs):

    prefix = strs[0]

    for i in range(1, len(strs)):

        # if substring is found, it will return the first index
        # if that element isn't the first char, then chop off
        while strs[i].find(prefix) != 0:

            # keep chopping off the last character
            prefix = prefix[0: len(prefix)-1]
            if not prefix: return ""
        
    return prefix

    # for s in strs:

    #     # compare s to longest
    #     for i in range(len(s)):
    #         print(s[i], longest[i])
    #         if s[i]==longest[i]:
    #             continue
    #         else:
    #             longest = longest[:i]   # cut off longest to length of common characters of s
    
    #         print("longest: ", flower)

    # return prefix

print( lcp(strs) )