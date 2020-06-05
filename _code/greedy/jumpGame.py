arr = [2,3,1,1,4]

def canJump(nums) -> bool:
    
    lastPos = len(nums) - 1
    for i in reversed(range(len(nums))):
        
        print(i, nums[i], lastPos)

        if i + nums[i] >= lastPos:
            lastPos = i
    
    return lastPos == 0

canJump(arr)