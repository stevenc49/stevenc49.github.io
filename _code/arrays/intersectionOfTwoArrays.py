from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        map = {}
        for num in nums1:
            if num not in map:
                map[num] = 1
            else:
                map[num] = map[num] + 1


        for k,v in map.items():
            print( k, v)

        # iter thru num2, if exist in map, minus it
        res = []
        for num in nums2:
            if num in map:
                res.append(num)
                if map[num]>1:
                    map[num] = map[num]-1
                else:
                    map.pop(num)

        print(res)

        # set1 = set(nums1)
        # set2 = set(nums2)

        # res = set1.intersection(set2)
        # return list(res)


nums1 = [1,1,2,2]
nums2 = [2,2]
print( Solution().intersect(nums1, nums2) )