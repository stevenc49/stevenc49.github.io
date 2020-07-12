nums = [1,2,3]


# def subsets(nums):

#     def backtrack(first = 0, curr = []):
#         # if the combination is done
#         if len(curr) == k:  
#             output.append(curr[:])
#         for i in range(first, n):
#             # add nums[i] into the current combination
#             curr.append(nums[i])
#             # use next integers to complete the combination
#             backtrack(i + 1, curr)
#             # backtrack
#             curr.pop()
    
#     output = []
#     n = len(nums)
#     for k in range(n + 1):
#         backtrack()
#     return output


def subsets(nums):
    subsets = []
    
    def generateSubsets(index, nums, current, subsets):
        subsets.append(current[:])
        for i in range(index, len(nums)):
            current.append(nums[i])
            generateSubsets(i + 1, nums, current, subsets)
            current.remove(current[-1])
            
    generateSubsets(0, nums, [], subsets)
    return subsets


def subsets2(nums):

    def backtrack(startIndex, currentSubset, allSubsets, nums):

        allSubsets.append(currentSubset[:])

        for i in range(startIndex, len(nums)):
            currentSubset.append(nums[i])
            print(currentSubset)

            backtrack( i+1, currentSubset, allSubsets, nums)
            
            currentSubset.remove( currentSubset[-1] )
            print(currentSubset)

    allSubsets = []
    backtrack( 0, [], allSubsets, nums )
    return allSubsets



def subsets3(nums):

    def backtrack(currentSubset, allSubsets, nums, index):

        allSubsets.append( currentSubset.copy() )

        for i in range(index, len(nums)):

            currentSubset.append(nums[i])
            print(currentSubset)

            backtrack( currentSubset, allSubsets, nums, i+1 )
            currentSubset.pop()
            print(currentSubset)


    ans = []
    backtrack([], ans, nums, 0)
    return ans


def subsets5(nums):

    def helper(index, currentSubset, allSubsets):

        output.append( currentSubset.copy() )

        for i in range(index, len(nums) ):

            currentSubset.append( nums[i] )
            helper(i+1, currentSubset, output)
            currentSubset.pop()
        
    output = []
    helper(0, [], output)
    return output



'''
    recursion without backtracking from timonthy chang
    https://www.youtube.com/watch?v=Mi_C_CMW7vQ
'''
def subsets4(nums):

    output = []

    def helper(start, tmp, output):
        # output += [tmp]
        output.append(tmp)
        for i in range(start, len(nums)):
            print( (i+1, tmp+[nums[i]]) )
            helper( i+1, tmp+[nums[i]], output )
    
    helper(0, [], output)

    return output


# print(subsets2(nums))
# print()
# print(subsets3(nums))
print(subsets4(nums))
print(subsets5(nums))
