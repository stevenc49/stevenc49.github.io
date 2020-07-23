arr = [1,2,3,4,5]


def binarySearch(left, right, arr, target):

    print(left, right, arr, target)
    print( right, left, right<=left )

    while left<=right:

        
        print(left, right, arr, target)

        mid = int((left+right)/2)
        # mid = left+right//2

        if arr[mid]==target:
            return mid
        
        elif target>arr[mid]:
            left = mid+1
        else:
            right = mid-1
        
    return -1


print(binarySearch(0, len(arr)-1, arr, 4))