
# map and lambda
arr = [1,2,3]
sqrt = map(lambda x: x*x, arr)
print(arr)
print( list(sqrt) )


# list comprehension
# Find all of the numbers from 1-1000 that are divisible by 7
# results = [num for num in range(1000) if num % 7 == 0]
# print(results)

# res = []
# for n in range(1000):
#     if n % 7 == 0:
#         res.append(n)
# print(res)


# new_list = [expression(i) for i in old_list if filter(i)]
new_list = [i**2 for i in range(1,10) if i>5]
print(new_list)

arr = [1,6,7,5,9]
list2 = [ i/2 for i in arr if i > 3 ]   # expression happens first, then the filter on i happens before the expression
print( list2 )

# zip


print("start fib testing")

def fib(n):

    res = [ 0 for i in range(n) ]
    res[1] = 1

    i=3
    while i<=n:

        res[i-1] = res[i-2] + res[i-3]
        i+=1
    
    print(res)


fib(3)
fib(4)
fib(10)

