'''
Find Subsequence of Length K With the Largest Sum

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
'''


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        maxSum = 0
        res = []

        for i in range(len(nums)-k+1):

            sum=0
            for j in range(i, i+k):
                sum+=nums[j]
            
            if sum>maxSum:
                maxSum = sum
                res = nums[i:j+1]
            
        return res
