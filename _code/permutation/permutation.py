# nums = [10,20,30]
nums = [1,1,2]

def permute1(nums):

    def backtrack(currentList, allPermutations, nums):

        if len(currentList)==len(nums):
            allPermutations.append(currentList[:])  # or currentList.copy() because Python passes by reference
        else:
            for i in range(0, len(nums)):
                if nums[i] in currentList:
                    continue
                currentList.append(nums[i])
                backtrack( currentList, allPermutations, nums )
                currentList.remove(currentList[-1])   # currentList.pop() also does the same thing


    allPermutations = []
    backtrack([], allPermutations, nums)
    return allPermutations


def permute2(nums):

    def backtrack(currentList, allPermutations, nums):

        if len(currentList)==len(nums):
            allPermutations.append(currentList.copy())
        else:
            for i in range(len(nums)):

                currentList.append(nums[i])
                print(currentList)

                backtrack(currentList, allPermutations, nums)
                currentList.pop()
                print(currentList)


    allPermutations = []
    backtrack([], allPermutations, nums)
    return allPermutations

# print(permute1(nums))
# print()
print(permute2(nums))