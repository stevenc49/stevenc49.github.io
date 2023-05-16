

arr = [1,2,3,4,5,6]
k = 3

for i in range(len(arr) - k + 1):

    sum = 0

    for j in range(i, i+k):

        print(arr[j])

    print()

