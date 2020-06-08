nums = [4,5,6,7,2,3]
target = 1

def search(nums, target):

    left = 0
    right = len(nums)-1

    # this loop gets left to the smallest element
    while left<right:

        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid


print( search(nums, target) )