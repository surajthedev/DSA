# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000





# Brute force:
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []

        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2 and num1 not in result:
                    result.append(num1)

        return result





# Optimal:
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        result = set()

        for num in nums2:
            if num in set1:
                result.add(num)

        return list(result)