height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):

    left = 0
    right = len(height)-1

    maxArea = 0

    while left<right:

        minHeight = min( height[left], height[right] )
        distance = right-left

        maxArea = max( maxArea, minHeight*distance )

        # move shorter one inward
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    
    return maxArea


print(maxArea(height))