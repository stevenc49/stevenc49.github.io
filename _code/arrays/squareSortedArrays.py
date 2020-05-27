

def main():

    arr = [-3,-2,-1,0,1,2,3]

    # move ptrs to middle section, j moves forward, i moves backwards
    j = 0
    while arr[j]<0:
        j+=1

    i=j-1


    # create new array to store results
    ans = []
    while i>=0 and j<len(arr):

        print arr[i]
        print arr[j]
        print ''

        if arr[i]**2 < arr[j]**2:
            ans.append( arr[i]**2 )
            i-=1
        else:
            ans.append( arr[j]**2 )
            j+=1

    print ans




if __name__ == "__main__":
    main()
