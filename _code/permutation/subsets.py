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

        print(currentSubset)

        allSubsets.append(currentSubset[:])

        for i in range(startIndex, len(nums)):
            currentSubset.append(nums[i])
            backtrack( i+1, currentSubset, allSubsets, nums)
            currentSubset.remove( currentSubset[-1] )

    allSubsets = []
    backtrack( 0, [], allSubsets, nums )
    return allSubsets


print(subsets2(nums))