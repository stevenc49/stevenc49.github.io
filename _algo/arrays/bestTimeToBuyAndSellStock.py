import sys

arr = [7,1,5,3,6,4]
# arr = [7,6,4,3,1]
# arr = [2,4,1]

def maxProfit(arr):

    if not arr or len(arr)==0:
        return 0
    
    maxProfit = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j]-arr[i]>maxProfit:
                maxProfit = arr[j]-arr[i]
    
    return maxProfit


print(maxProfit(arr))