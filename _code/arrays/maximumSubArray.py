'''

    Given an array of integers and a number k, find maximum sum of a subarray of size k.

    11:40

    https://medium.com/hackernoon/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed#6698
    https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/
'''


def main():

    # arr = [1,2,3,4,2]
    # k = 2

    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    k = 4

    maxSum = 0

    for i in range(0, len(arr)-k+1 ):

        sum = 0

        for j in range(0, k):

            # set j to beginning of window
            j=i

            sum = sum + arr[j]

            i+=1

        print sum

        if sum > maxSum:
            maxSum = sum

    print 'max sum is ' + str(maxSum)




if __name__ == "__main__":
    main()
