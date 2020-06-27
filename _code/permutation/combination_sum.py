candidates = [2,3,6,7]
target = 7

def combinationSum(candidates, target):
    
    def backtrack(currentList, nums, start):
        
        if sum(currentList)==target:
            allValidCombos.append( currentList.copy() )
            return 
        if sum(currentList) > target: # optimization
            return
        for i in range(start, len(nums)):
            backtrack(currentList + [nums[i]], nums, i)
            # currentList.append( nums[i] )
            # backtrack( currentList, nums, start)
    
    allValidCombos = []
    backtrack([], candidates, 0 )
    return allValidCombos

print( combinationSum(candidates, target) )