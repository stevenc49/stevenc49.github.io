arr = [0,1,0,1,1,0,0,1]
N=7


def prisonAfterNDays(arr, N):

    arr2 = [0]*len(arr)

    for i in range(N):

        for i in range(1, len(arr)-1):
            
            # not xor the middle
            arr2[i] = int(not arr[i-1] ^ arr[i+1])

            # make ends zero
            arr2[0], arr2[len(arr)-1] = 0,0

        # copy arr2 to arr
        arr = arr2.copy()
    
    return arr

print(prisonAfterNDays(arr, N))
