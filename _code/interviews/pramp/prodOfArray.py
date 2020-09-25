arr = [8,10,2]
# arr = [2,2]

def array_of_array_products(arr):
    #[8, 10, 2]
    # i = 0. left = [], right [10,2]
    res = []
    def helper(listt):
        prod = 1
        for val in listt:
            prod = prod*val
        return prod
  
    print(arr)
    print(helper(arr))

#   for i, val in enumerate(arr):
#     left = None
#     right = None
#     if i != 0:
#       left = helper(arr[:i])
#     if i != len(arr)-1:
#       right = helper(arr[i+1:])
#     if left and right:
#       res.append(left*right)
#     elif left:
#       res.append(left)
#     elif right:
#       res.append(right)
    return res
    
   
    
    

print( array_of_array_products(arr) )