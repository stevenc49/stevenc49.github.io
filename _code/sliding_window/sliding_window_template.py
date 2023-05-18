
'''

    Find the max sum subarray with size k
    [4,2,1,7,8,1,2,8,1,0] k=3

    1,7,8 produces 16
'''

def maxSubarray(arr, k):

    maxSum = 0

    for i in range(len(arr) - k + 1):

        sum = 0

        for j in range(i, i+k):

            sum += arr[j]
            print(arr[j])

            # if sum>maxSum:
            #     maxSum = sum

            print()

    return maxSum


def main():
    arr = [1, 2, 3, 4, 5, 6]
    k = 3

    res = maxSubarray(arr, k)
    print(res)

if __name__ == "__main__":
    main()
