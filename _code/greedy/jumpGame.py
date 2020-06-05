arr = [2,3,1,1,4]

def canJump(nums) -> bool:
    
    lastGoodPos = len(nums) - 1
    for i in reversed(range(len(nums))):
        
        print(i, nums[i], lastGoodPos, i + nums[i] >= lastGoodPos)

        if i + nums[i] >= lastGoodPos:
            lastGoodPos = i
    
    return lastGoodPos == 0

canJump(arr)