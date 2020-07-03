arr = [0,1,0,1,1,0,0,1]
N=6

def prisonAfterNDays(arr, N):

    def computeNext(arr):

        arr2 = [0]*len(arr)
        
        for i in range(1, len(arr)-1):
            
            # not xor the middle
            arr2[i] = int(not arr[i-1] ^ arr[i+1])

            # make ends zero
            arr2[0], arr2[len(arr)-1] = 0,0

        # copy arr2 to arr
        return arr2.copy()


    memo = {}

    for i in range(N):

        if tuple(arr) not in memo:
            old_arr = arr
            new_arr = computeNext(arr)

            memo[tuple(old_arr)] = new_arr
            arr = new_arr
        else:
            arr = memo[tuple(arr)]

    print(memo)
    return arr

print( prisonAfterNDays(arr, N) )