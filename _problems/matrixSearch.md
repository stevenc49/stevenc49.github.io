---
layout: page
title:  Matrix Search
---

Trick:
- think of matrix as 1D array
- turn 1D array index to row/col mapping
- ie: to access 16 (in array index 6), we know row=1 and col=2
- the magic leap is to realize row=6//4 and col=6%4 or ```(index//col_len``` and ```index%col_len)```


Gotcha:
- if you don't get a handle on your off by one errors, you'll run into infinite loops
- row is mid//col_len, not mid//row_len



{% highlight python %}

# mat = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]

mat = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]


def searchMatrix(mat, target):

    if not mat: return False
    
    row_len=len(mat)
    col_len=len(mat[0])
    
    low = 0
    high = row_len * col_len -1
    
    while low<=high:
        
        mid = (low+high)//2
        
        print(low, high, mid)
        
        if mat[mid//col_len][mid%col_len]==target:
            return True
        elif mat[mid//col_len][mid%col_len]<target:
            low = mid+1
        else:
            high = mid-1
    
    return False


print(searchMatrix(mat, 13))

{% endhighlight %}


![image1]()