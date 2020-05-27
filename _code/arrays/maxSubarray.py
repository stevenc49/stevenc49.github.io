arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubarray(arr):

    if not arr:
        return None

    for i in range(len(arr)):

        if i==0:
            continue
        else:
            arr[i] = max(arr[i], arr[i-1] + arr[i])     # max of "start with this elem" or "continue the existing subarray"
    
    
    return max(arr)




print(maxSubarray(arr))