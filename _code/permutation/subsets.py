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

print(subsets(nums))