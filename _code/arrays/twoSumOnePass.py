nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):

    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
    return []


res = twoSum(nums, target)
print (res)
