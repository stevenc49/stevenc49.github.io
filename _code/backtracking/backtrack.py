import sys

sys.setrecursionlimit(10)

nums = [1,2,3]

def permute(nums):

    output = []

    def backtrack(currentList):

        print(currentList)

        # base case
        if len(currentList)==len(nums):
            output.append(currentList.copy())
        
        # imagine you're at [1] (your currentList) and you want to append 1,2,3 to your child branches
        # so they become 11, 12, 13
        for i in range(0, len(nums)):

            if nums[i] in currentList:
                continue

            currentList.append(nums[i])
            backtrack(currentList)
            currentList.pop()
    
    backtrack([])
    return output


print( permute(nums) )