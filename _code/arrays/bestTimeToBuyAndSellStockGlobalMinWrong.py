import sys

arr = [7,1,5,3,6,4]
arr = [7,6,4,3,1]
arr = [2,4,1]

def maxProfit(arr):

    if not arr or len(arr)==0:
        return 0
    

    # find lowest pt
    globalMin = sys.maxsize
    globalMinIndex = -1
    for i in range(len(arr)):
        if arr[i]<globalMin:
            globalMin=arr[i]
            globalMinIndex=i


    globalMax = -sys.maxsize
    globalMaxIndex = -1
    # starting from globalMinIndex, find the max value
    for i in range(globalMinIndex+1, len(arr)):
        if arr[i]>globalMax:
            globalMax=arr[i]
            globalMaxIndex=i

    print(globalMinIndex, globalMaxIndex)

    if globalMaxIndex!=-1:      # a max was found after global min
        return globalMax-globalMin
    else:
        return 0


print(maxProfit(arr))