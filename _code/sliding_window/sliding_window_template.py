
'''

    Find the max sum subarray with size k
    [4,2,1,7,8,1,2,8,1,0] k=3

    1,7,8 produces 16

    https://www.youtube.com/watch?v=MK-NZ4hN7rs
'''


'''
    my solution - may 17, 2023
'''
def maxSubarray(arr, k):
    maxSum = 0

    for i in range(len(arr) - k + 1):
        sum = 0

        for j in range(i, i + k):
            print(arr[j])
            sum = sum + arr[j]

        maxSum = max(sum, maxSum)

        print("sum: " + str(sum))
        print("maxSum: " + str(maxSum))

        print()
    return maxSum


def main():
    arr = [4,2,1,7,8,1,2,8,1,0]
    k = 3

    res = maxSubarray(arr, k)
    print(res)

if __name__ == "__main__":
    main()
