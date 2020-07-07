nums = [2,5,3,4,5]
nums = [6,5,3,4,0]

def increasingTriplet(nums):
    
    first = nums[0]
    second = float('inf')
    third = float('inf')

    for n in nums:

        if n<first:
            first = n
        elif n>first and n<second:
            second = n
        elif n>second and n<third:
            third = n
    
    print(first, second, third)

    return third!=float('inf')


print(increasingTriplet(nums))