nums1 = [1,2,2,1]
nums2 = [2,2]


def intersect(nums1, nums2):

    nums1.sort()
    nums2.sort()

    i=0
    j=0

    #1,1,2,2
    #2,2

    ans = []
    
    # logic is similar to merging
    while( i <= len(nums1)-1 and j <= len(nums2)-1 ):

        if nums1[i]==nums2[j]:
            ans.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
        else:
            j+=1
    
    return ans


print( intersect(nums1, nums2) )