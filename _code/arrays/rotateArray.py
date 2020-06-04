arr = [1,2,3,4,5,6,7]
arr = [-1]
arr = [1,2]

def rotate(nums, k):

	if not nums: return
	if len(nums) == 1: return

	def reverse(nums, start, end):

		while start < end:
			tmp = nums[start]
			nums[start] = nums[end]
			nums[end] = tmp

			start += 1
			end -= 1

	reverse(nums, 0, len(nums) - 1)
	reverse(nums, 0, k - 1)
	reverse(nums, k, len(nums) - 1)

rotate(arr, 3)

print(arr)