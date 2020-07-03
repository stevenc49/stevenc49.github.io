arr = [0,1,0,1,1,0,0,1]
N=1000000000
# N=7

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



    seen = {str(arr): N}
    while N:
        seen.setdefault(str(arr), N)
        N -= 1
        # arr = [0] + [arr[i - 1] ^ arr[i + 1] ^ 1 for i in range(1, 7)] + [0]
        arr = computeNext(arr)
        if str(arr) in seen:
            N %= seen[str(arr)] - N
        
    return arr


print( prisonAfterNDays(arr, N) )