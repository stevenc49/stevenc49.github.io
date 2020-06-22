nums = [10,20,30]

def backtracking(res,visited,subset,nums):

    print(res, visited, subset)

    if len(subset) == len(nums):
        res.append(subset)
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(res,visited,subset+[nums[i]],nums)
            visited.remove(i)

def permute(nums):
    visited = set()
    res = []
    backtracking(res,visited,[],nums)
    return res

print(permute(nums))