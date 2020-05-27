arr = [4,5,6,7,2,3]

def findMin(nums):

    l, r = 0, len(nums)  - 1
    while nums[l] > nums[r]:
        mid =  int((l+r)/2)  
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid
    return nums[l]

print(findMin(arr))
