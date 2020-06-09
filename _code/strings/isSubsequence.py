s = "abc"
t = "ahbgdc"


def isSubsequence(s, t):

    sp = 0
    tp = 0

    while sp<len(s) and tp<len(t):

        if s[sp]==t[tp]:
            sp+=1
            tp+=1
            continue
        else:
            tp+=1

    # reached end of s
    return sp==len(s)


# def isSubsequence(s, t):

#     sp = 0
#     tp = 0

#     while sp < len(s):

#         # increment tp until a match
#         while sp<len(s) and tp<len(t) and s[sp]!=t[tp]:
#             tp+=1

#         # reached end of t
#         if tp==len(t):

#             if t[tp-1]==s[sp]:
#                 return True
#             else:
#                 return False
        

#         # if there's a match, increment both
#         if s[sp]==t[tp]:
#             sp+=1
#             tp+=1


print( isSubsequence(s,t) )
