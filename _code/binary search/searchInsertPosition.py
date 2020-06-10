def searchInsert(nums, target):

    left = 0
    right = len(nums)-1

    while left<=right:

        mid = (left+right)//2

        if target==nums[mid]:
            return mid

        # # left and right beside each other
        # elif right-left<=1:

        #     # and target is inbetween (ie: [4,6], tar=5)
        #     if target>=nums[left] and target<=nums[right]:
        #         return left+1

        #     # target is outside of array (to the right)
        #     elif target>nums[right]:
        #         return right+1
            
        #     # target is outside of array (to the left)
        #     elif target<nums[left]:
        #         return left

        elif target>nums[mid]:
            left = mid+1
        elif target<nums[mid]:
            right = mid-1

    return left



print( searchInsert( [1,3,5,6] , 5) )   # 2
print( searchInsert( [1,3,4,6] , 5) )   # 3
print( searchInsert( [1,2] , 3) )   # 2
print( searchInsert( [1,2] , 0) )   # 0
print( searchInsert( [1,3] , 2) )   # 1