# mat = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

def searchMatrix(mat, target):

    rows = len(mat)
    cols = len(mat[0])

    start = 0
    end = rows * cols - 1

    while start<=end:

        mid = (start+end)//2      # this would be the mid if it was a 1d array
        row = mid // cols
        col = mid % cols
        val=mat[row][col]

        if val==target:
            return True
        elif val<target:
            start=mid+1
        else:
            end=mid-1

    return False


print(searchMatrix(mat, 13))