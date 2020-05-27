# arr = [1,2,3,4,5,6,7,8,9,10]
arr = [1,2,3,4,5]


def binSearch(low, high, arr, target):

    while low<=high:

        print(low, high, arr, target)

        mid = int((low+high)/2)
        # mid = low+high//2

        if arr[mid]==target:
            return mid

        # if target is greater, ignore left half
        elif arr[mid]<target:
            low = mid+1


        # if target is less, ignore right half
        else:
            high = mid-1


    return -1

res = binSearch(0, len(arr), arr, 4)
print(res)

