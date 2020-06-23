nums = [10,20,30]

# def backtracking(res,visited,subset,nums):

#     print(res, visited, subset)

#     if len(subset) == len(nums):
#         res.append(subset)
#     for i in range(len(nums)):
#         if i not in visited:
#             visited.add(i)
#             backtracking(res,visited,subset+[nums[i]],nums)
#             visited.remove(i)

# def permute(nums):
#     visited = set()
#     res = []
#     backtracking(res,visited,[],nums)
#     return res

def permute(nums):

    def backtrack(currentList, allPermutations, nums):

        if len(currentList)==len(nums):
            allPermutations.append(currentList[:])
        else:
            for i in range(0, len(nums)):
                if nums[i] in currentList:
                    continue
                currentList.append(nums[i])
                backtrack( currentList, allPermutations, nums )
                currentList.remove(currentList[-1])

    allPermutations = []
    backtrack([], allPermutations, nums)
    return allPermutations

print(permute(nums))