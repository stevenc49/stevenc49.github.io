

# ans = []
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         for k in range(j, len(nums)):
#             if nums[i] + nums[j] + nums[k] == 0:
#                 ans.append([nums[i], nums[j], nums[k]])

nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0]


def threeSum(nums):

    nums.sort()
    output = []

    index = 0
    while index<len(nums):

        # if nums[index]==nums[index+1]:
        #     print(index, nums[index], output)
        #     index+=1

        # if index>0 and nums[index]==nums[index-1]: continue #[1]

        fixed = nums[index]     # -1
        target = fixed*-1       # want to find 1 in rest of array

        l,r = index+1, len(nums)-1

        while l<r:

            if nums[index] + nums[l] + nums[r] == 0:
                output.append( [nums[index], nums[l], nums[r]] )
            
            l+=1
            r-=1
        

        index+=1
    
    return output



print(threeSum(nums))

